from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {"form": form})