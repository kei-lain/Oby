from django.contrib import admin
from django.urls import path , include
from .views import videoView , videoUpload

urlpatterns = [
    path('',videoView.as_view(), name='home screen'),
    path('', videoUpload.as_view(), name='video upload screen')
]
