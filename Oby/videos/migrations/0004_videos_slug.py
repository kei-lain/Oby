# Generated by Django 4.0.6 on 2022-07-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videos_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
    ]
