from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Student_number', 'first_name', 'last_name', 'email', 'course', 'gpa']  # Corrected 'field' to 'fields'
        labels = {
            'Student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'course': 'Course',
            'gpa': 'GPA',
        }
        widgets = {
            'Student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }