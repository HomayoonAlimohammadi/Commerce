# Generated by Django 4.0.2 on 2022-03-01 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0010_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auction.bid'),
        ),
    ]
