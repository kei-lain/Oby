import django_filters
from django.db import models
from .models import Channel

class ChannelFilter(django_filters.FilterSet):
    class Meta:
        model = Channel
        fields = ['channel_owner']