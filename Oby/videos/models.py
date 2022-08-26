from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=240)
    def __str__(self):
        return self.category_name

class Videos(models.Model):
    video = models.FileField(upload_to='media/videos/%Y/%m/%d/', 
    )
    video_title = models.CharField(max_length=500, blank = False, null = False , help_text= 'Please Enter a video title')
    video_description = models.CharField(max_length= 2000,help_text='Please put the video description here')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    

    def get_queryset(self):
        return(super(Videos, self).get_queryset())

    # def get_absolute_url(self):
    #     return reverse ("deploy:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.video_description 

    class Meta:
        ordering = ['date_uploaded']    


    