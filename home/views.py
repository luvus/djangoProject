from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return HttpResponse("Hello , Mihaela")


def details_student(request):
    details = {
        'all_students': [
            {
             'first_name': 'Mihaela',
             'last_name': 'Florescu',
             'hobby': 'alge_microscopice'
             },
            {
             'first_name': 'George',
             'last_name': 'Popovici',
             'hobby': 'ciclism'
            }
        ]
    }

    return render(request, 'details_student.html', details)

def details_teacher(request):
    details_teacher ={
        'all_teachers':[
            {
            'first_name_teacher':'Andreea',
            'last_name_teacher': 'Georgescu',
            'materia':'matematica'},
            {
                'first_name_teacher': 'Marian',
                'last_name_teacher': 'Andrei',
                'materia': 'biologie'}
    ]}
    return render(request, 'details_teacher.html', details_teacher)

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

