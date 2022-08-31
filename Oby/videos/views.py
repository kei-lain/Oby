from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.list import ListView
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .filters import VideoFilter
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, PermissionRequiredMixin
from .models import Videos, Categories
from .forms import VideoUpload 

# Create your views here.
class videoView(ListView):
    model = Videos
    template_name = 'videos/videowall.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = Videos.objects.filter(private=False)
        return context
    

    
    

class videoUpload(LoginRequiredMixin,CreateView):
    
    model = Videos
    fields = '__all__'
    template_name = 'videos/video_upload.html'
    success_url = reverse_lazy('home screen')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Categories.objects.all() 
        return context
    

class CategoryCreation(LoginRequiredMixin, CreateView):
    model = Categories
    fields = '__all__'
    template = 'videos/category_creation.html'

class WatchPage(DetailView):
    model = Videos
    context_object_name = 'video'
    template_name = 'videos/video_page.html'

class creatorDashboard(DetailView):
    template_name = 'videos/public_creator_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = Videos.objects.filter(uploaded_by=request.user)
        context["user"] = User.objects.filter(request.user)
        return context
    
   
    