# Generated by Django 4.0.6 on 2022-08-23 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_videos_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='slug',
        ),
    ]