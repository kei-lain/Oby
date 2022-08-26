import django_filters
from django.db import models
from .models import Videos

class VideoFilter(django_filters.FilterSet):
    class Meta:
        model = Videos
        fields = ['user']
    
