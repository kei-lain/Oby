from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length= 200,required=True, help_text='First Name')
    last_name =  forms.CharField(max_length=200, required=True  ,help_text='Last Name')
    email = forms.EmailField(required=True, help_text= 'Enter a valid email address')
    username = forms.CharField(required=True, help_text='Enter your desired Username')
    birthDate = forms.DateField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email' , 'username', 'birthDate')
