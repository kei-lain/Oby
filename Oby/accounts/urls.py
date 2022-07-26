from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('HOME', views.home, name='home'),
    path('sign-up', views.sign_up, name ='sign-up')
]
