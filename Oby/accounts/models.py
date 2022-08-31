from django.db import models
from django.contrib.auth.models import User
from videos.models import Videos , Categories
from django.conf import settings

# Create your models here.

class Channel(models.Model):
    channel_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    channel_name = models.CharField(max_length=250 , blank=False)
    channel_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    channel_description = models.TextField(max_length=2000)
    channel_icon = models.FileField(upload_to=f'media/images/icons/{channel_owner}/')

