from django.contrib import admin
from django.urls import path , include
from .views import customRegistrationView , profileView , channelCreation
urlpatterns = [
    # path('', views.home, name='home'),
    path('sign-up', customRegistrationView.as_view(), name ='sign-up'),
    path('profile/<int:pk>/',profileView.as_view(), name='profile'),
    path('channel-creation/', channelCreation.as_view(), name='channel creation')
]
