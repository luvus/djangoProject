
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from animals.forms import AnimalForm
from animals.models import Animals


class AnimalsCreateView(CreateView):
    template_name ='animals/create_animals.html'
    model = Animals
    success_url = reverse_lazy('create-new-animal')
    form_class = AnimalForm


