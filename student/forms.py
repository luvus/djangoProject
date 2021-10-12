from django import forms
from django.forms import TextInput

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'age', 'cnp', 'date_of_birth', 'email']
        # fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                           'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name',
                                          'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Please enter you age',
                                    'class': 'form-control'}),
            'cnp': TextInput(attrs={'placeholder': 'Please enter you CNP number',
                                    'class': 'form-control'}),
            'date_of_birth': TextInput(attrs={'placeholder': 'Please enter your date birth',
                                              'class': 'form-control', 'type': 'date'}),
            'email': TextInput(attrs={'placeholder': 'Please enter your email adress',
                                      'class': 'form-control'})

        }
