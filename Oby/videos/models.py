from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=240)
    def __str__(self):
        return self.category_name

class Videos(models.Model):
    video_title = models.CharField(max_length=500, blank = False, null = False , help_text= 'Please Enter a video title')
    video_description = models.CharField(max_length= 2000,help_text='Please put the video description here')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    video = models.FileField(upload_to=f'media/videos/{uploaded_by}/%Y/%m/%d/' )
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    

    def get_queryset(self):
        return(super(Videos, self).get_queryset())

    # def get_absolute_url(self):
    #     return reverse ("deploy:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.video_description 

    class Meta:
        ordering = ['date_uploaded']    


    