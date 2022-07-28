from django.shortcuts import render
from django.urls import  reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
# Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def sign_up(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#     else:
#         form = RegistrationForm()
#     return render(request, 'registration/sign_up.html', {"form": form})

class customRegistrationView(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = RegistrationForm
    fields: '__all__'
    redirected_authenticated_user = True
    reverse_lazy =('/login')
    success_url = '/login'
    def get_object(self):
        return self.request.user

    # def get_absolute_url():
    #     return reverse_lazy('sign in') def get_object(self):
    #     return self.request.user

    # def get_absolute_url():
    #     return reverse_lazy('sign in')


