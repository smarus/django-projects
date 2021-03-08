from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from resume.forms import ResumeForm, VacancyForm


def index(request):
    return render(request, "hyperjob/index.html")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_staff:
            vacancy_form = VacancyForm()
            context['postcard_form'] = vacancy_form
            context['type'] = 'vacancy'
        else:
            resume_form = ResumeForm()
            context['postcard_form'] = resume_form
            context['type'] = 'resume'
        return render(request, template_name='form.html', context=context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'hyperjob/signup.html'
    success_url = 'login'


class Login(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'
