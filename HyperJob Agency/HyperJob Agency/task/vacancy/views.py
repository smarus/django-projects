from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from django.views import View
from .models import Vacancy
from resume.forms import VacancyForm


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        values = Vacancy.objects.all()
        context = {"vacancies": values}
        return render(request, context=context, template_name='vacancy/vacancy.html')


class CreateVacancy(View):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.is_staff:
            raise PermissionDenied

        vacancy_form = VacancyForm(request.POST)
        if vacancy_form.is_valid():
            user = request.user
            resume = Vacancy(description=vacancy_form.cleaned_data['description'], author=user)
            resume.save()
            return redirect('/home')
        else:
            raise PermissionDenied
