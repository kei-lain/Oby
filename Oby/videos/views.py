from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.list import ListView
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from .models import Videos
from .forms import VideoUpload

# Create your views here.
class videoView(ListView):
    model = Videos
    context_object_name =  'videos'
    template_name = 'videos/videowall.html'

        
    

    # def get_queryset(self, *args, **kwargs):
    #     qs = Videos.objects.all()
    #     print(self.request.GET)
    #     query = self.request.GET.get("q", None)
    #     if query is not None:
    #         qs = qs.filter(
    #              Q(video_description__icontains=query) | Q(video__icontains=query)
    #         )
    #     return qs
    
    # def get_context_data(self, *args,**kwargs):
    #     context = super( videoView, self).get_context_data(*args, **kwargs)
    #     return context
    
    

class videoUpload(LoginRequiredMixin,CreateView):
    
    model = Videos
    fields = '__all__'
    template_name = 'videos/video_upload.html'
    success_url = reverse_lazy('home screen')

class WatchPage(DetailView):
    model = Videos
    context_object_name = 'video'
    template_name = 'videos/video_page.html'
   
    