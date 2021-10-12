from django import forms
from django.forms import TextInput
from animals.models import Animals



class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['name_of_animal', 'species', 'date_of_vaccination', 'email_of_owner']
        widgets = {'name_of_animal': TextInput(attrs={'placeholder':'Please enter your animal name',
                                                      'class':'form-control'}),
                   'species': TextInput(attrs={'placeholder':'Please add the species',
                                               'class':'form-control'}),
                   'date_of_vaccination': TextInput(attrs={'placeholder':'Please add the date',
                                                           'class' : 'form-control'}),
                   'email_of_owner': TextInput(attrs={'placeholder' : 'Please add the email',
                                                      'class':'form-control'})
                   }