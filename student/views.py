
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from student.forms import StudentForm
from student.models import Student


class StudentCreateView(CreateView):
    template_name = 'student/create_student.html'
    model = Student
    success_url = reverse_lazy('create-new-student')
    form_class = StudentForm


class StudentListView(ListView):
    template_name = 'student/list_students.html'
    model = Student
    context_object_name = 'all_students'


class StudentUpdateView(UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')


class StudentDetailView(DetailView):
    template_name = 'student/detail_student.html'
    model = Student


class StudentDeleteView(DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
