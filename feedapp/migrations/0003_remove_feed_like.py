# Generated by Django 4.2 on 2023-05-24 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feedapp", "0002_feed_like_feed_like_cnt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feed",
            name="like",
        ),
    ]
