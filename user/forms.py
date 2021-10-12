from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from user.models import ExtendUser


class UserForm(UserCreationForm):
    class Meta:
        model = ExtendUser
        fields = ['first_name', 'last_name', 'email', 'username', 'age', 'date_of_birth', 'county']
        widgets = {'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                                  'class': 'form-control'}),
                   'last_name': TextInput(attrs={'placeholder': 'Please enter your last name',
                                                 'class': 'form-control'}),
                   'email': TextInput(attrs={'placeholder': 'Please enter your email address',
                                             'class': 'form-control'}),
                   'username': TextInput(attrs={'placeholder': 'Please enter your username',
                                                'class': 'form-control'}),
                   'age': TextInput(attrs={'placeholder': 'Please enter your age',
                                           'class': 'form-control'}),
                   'date_of_birth': TextInput(attrs={'placeholder': 'Please enter your date of birth',
                                                     'class': 'form-control', 'type': 'date'})

                   }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please re-enter your password'
