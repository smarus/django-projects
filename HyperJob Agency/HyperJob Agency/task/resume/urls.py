from django.urls import path
from django.views.generic import RedirectView
from .views import ResumeView, CreateResume

app_name = "resume"

urlpatterns = [
    path('resumes', ResumeView.as_view(), name="resume"),
    path('resume/new/', RedirectView.as_view(url='resume/new')),
    path('resume/new', CreateResume.as_view(), name="new")
]