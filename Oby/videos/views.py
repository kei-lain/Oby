from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from .models import Videos

# Create your views here.
class videoView(ListView):
    model = Videos
    context_object_name =  'videos'
    template_name = 'videos/videowall.html'

class videoUpload(LoginRequiredMixin,CreateView):
    model = Videos
    fields = '__all__'
    template_name = 'videos/video_upload.html'
    reverse_lazy =('home/')
    
    