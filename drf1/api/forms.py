from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta():
        fields = ['name','roll_no','city']
        model = Student
