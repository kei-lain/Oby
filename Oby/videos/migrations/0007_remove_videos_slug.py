# Generated by Django 4.0.6 on 2022-08-02 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_videos_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='slug',
        ),
    ]