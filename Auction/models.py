from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('auction:category', args=[self.name])


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    watchers = models.ManyToManyField(User, related_name='watchlist', blank=True)
    category = models.ManyToManyField(Category, related_name='listings', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starting_price = models.FloatField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    current_bid = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def serialize(self):

        return {
            'id': self.id,
            'title': self.title,
            'user': self.user.username,
            'category': [category.name for category in self.category.all()],
            'starting_price': self.starting_price,
            'current_bid': self.current_bid.amount if self.current_bid else None,
            'current_bidder': self.current_bid.user.username if self.current_bid else None,
            'is_active': self.is_active,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M'),
        }
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Listing)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Listing` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Listing)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Listing` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_file = Listing.objects.get(pk=instance.pk).image
    except Listing.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)