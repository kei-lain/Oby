from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to='videos_uploaded', null=True, 
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video_title = models.CharField(max_length=500, blank = False, null = False , help_text= 'Please Enter a video title')
    video_description = models.CharField(max_length= 2000,help_text='Please put the video description here')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_title

    class Meta:
        ordering = ['date_uploaded']    