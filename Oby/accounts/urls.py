from django.contrib import admin
from django.urls import path , include
from .views import customRegistrationView
urlpatterns = [
    # path('', views.home, name='home'),
    path('sign-up', customRegistrationView.as_view(), name ='sign-up')
]
