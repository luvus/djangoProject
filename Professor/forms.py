from django import forms
from django.forms import TextInput

from Professor.models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name_professor', 'last_name_professor', 'subject', 'date_of_employment', 'email']
        widgets = {'first_name_professor': TextInput(attrs={'placeholder': 'Please enter as professor the first name',
                                                            'class': 'form-control'}),
                   'last_name_professor': TextInput(attrs={'placeholder': 'Please enter as professor the last name',
                                                           'class': 'form-control'}),
                   'subject': TextInput(attrs={'placeholder': 'Please enter the subject that you teach',
                                               'class': 'form-control'}),
                   'date_of_employment': TextInput(attrs={'placeholder': 'Please enter the date',
                                                          'class': 'form-control', 'type': 'date'}),
                   'email': TextInput(attrs={'placeholder': 'Please add your email adress',
                                             'class': 'form-control'})
                   }
