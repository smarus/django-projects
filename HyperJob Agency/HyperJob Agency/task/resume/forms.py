from django import forms


class ResumeForm(forms.Form):
    description = forms.CharField(label="Description")


class VacancyForm(forms.Form):
    description = forms.CharField(label="Description")
