# Generated by Django 4.0.2 on 2022-02-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0008_alter_listing_category_alter_listing_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
