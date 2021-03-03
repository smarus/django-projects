from django.shortcuts import render
from django.views import View
from .models import Resume


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        values = Resume.objects.all()
        context = {"resumes": values}
        return render(request, context=context, template_name='resume/resume.html')
