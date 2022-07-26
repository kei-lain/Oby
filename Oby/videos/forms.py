from django.forms import ModelForm
from .models import Videos

class VideoUpload(forms.ModelForm):
    
    class Meta:
         fields ='__all__'
