# Generated by Django 5.0.4 on 2024-05-03 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_listing_price_bid_bid_bid_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_url',
        ),
    ]