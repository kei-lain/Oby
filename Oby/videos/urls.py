from django.contrib import admin
from django.urls import path , include
from .views import videoView , videoUpload

urlpatterns = [
    path('',videoView.as_view(), name='home screen'),
    path('home/',videoView.as_view(), name='home screen'),
    path('upload-video/', videoUpload.as_view(), name='video upload screen')
]
