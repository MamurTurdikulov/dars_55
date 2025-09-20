from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'})
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model=Groups
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'})
        }
