# Generated by Django 5.0.4 on 2024-05-03 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_comment_date_time_comment_listing_item_comment_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='current_highest_bid',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='title',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
    ]
