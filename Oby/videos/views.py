from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Videos

# Create your views here.
class videoView(ListView):
    model = Videos
    context_object_name =  'videos'
    template_name = 'videos/videowall.html'

class videoUpload(CreateView):
    model = Videos
    fields = '__all__'
    reverse_lazy =('/')
    
    