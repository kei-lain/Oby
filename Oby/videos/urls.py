from django.contrib import admin
from django.urls import path , include
from .views import videoView , videoUpload, WatchPage

urlpatterns = [
    path('',videoView.as_view(), name='home screen'),
    path('home/',videoView.as_view(), name='home screen'),
    path('video/<int:pk>/',WatchPage.as_view(), name= 'video' ),
    path('upload-video/', videoUpload.as_view(), name='video upload screen')
]
