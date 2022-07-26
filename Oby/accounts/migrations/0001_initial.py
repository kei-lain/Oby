# Generated by Django 4.0.6 on 2022-08-27 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0011_rename_user_videos_uploaded_by_videos_private_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=250)),
                ('channel_description', models.TextField(max_length=2000)),
                ('channel_icon', models.FileField(upload_to='media/images/icons/<django.db.models.fields.related.ForeignKey>/')),
                ('channel_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.categories')),
                ('channel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
