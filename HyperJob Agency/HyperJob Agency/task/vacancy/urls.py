from django.urls import path
from .views import VacancyView, CreateVacancy
from django.views.generic import RedirectView

app_name = "vacancy"
urlpatterns = [
    path('vacancies', VacancyView.as_view(), name="main"),
    path('vacancy/new/', RedirectView.as_view(url="/new")),
    path('vacancy/new', CreateVacancy.as_view(), name="new")
]