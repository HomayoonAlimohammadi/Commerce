from django.test import TestCase
from .models import Category, Comment, User, Listing, Bid

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('pazzo', password='1991')

    def test_user_password(self):
        checked = self.user_a.check_password('1991')
        self.assertTrue(checked)


class ListingTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user('homayoon', password='1991')
        self.user_2 = User.objects.create_user('nooshin', password='1991')
        self.listing_1 = Listing.objects.create(title='listing_1',
                                description='desc',
                                user=self.user_1,
                                starting_price=1000)
        self.category_1 = Category.objects.create(name='category_1')
        self.listing_1.category.add(self.category_1)

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_category_count(self):
        qs = self.listing_1.category.all()
        self.assertEqual(qs.count(), 1)
    
    def test_category_reverse_count(self):
        qs = self.category_1.listings.all()
        self.assertEqual(qs.count(), 1)




