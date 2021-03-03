from django.shortcuts import render

from django.views import View
from .models import Vacancy


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        values = Vacancy.objects.all()
        context = {"vacancies": values}
        return render(request, context=context, template_name='vacancy/vacancy.html')

