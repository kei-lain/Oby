from django.forms import ModelForm
from .models import Videos

class VideoUpload(ModelForm):
    class Meta:
         model = Videos
         fields ='__all__'
