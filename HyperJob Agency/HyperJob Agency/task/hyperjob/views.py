from django.shortcuts import render ,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import RedirectView


def index(request):
    return render(request, "hyperjob/index.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'hyperjob/signup.html'
    success_url = 'login'


class Login(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'
