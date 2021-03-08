from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Resume
from django.core.exceptions import PermissionDenied
from .forms import ResumeForm


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        values = Resume.objects.all()
        context = {"resumes": values}
        return render(request, context=context, template_name='resume/resume.html')


class CreateResume(View):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied

        resume_form = ResumeForm(request.POST)
        if resume_form.is_valid():
            print(resume_form.cleaned_data['description'])
            user = request.user
            resume = Resume(description=resume_form.cleaned_data['description'], author=user)
            resume.save()
            return redirect('/home')
        else:
            raise PermissionDenied
