from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from Professor.forms import ProfessorForm
from Professor.models import Professor


class ProfessorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    template_name = 'Professor/create_Professor.html'
    model = Professor
    success_url = reverse_lazy('create-new-professor')
    form_class = ProfessorForm
    permission_required = 'Professor.add_professor'


class ProfessorListView(ListView):
    template_name = 'Professor/lists_professor.html'
    model = Professor
    context_object_name = 'all_professors'


class ProfessorUpdateView(UpdateView):
    template_name = 'Professor/update_professor.html'
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('list-of-professor')


class ProfessorDetailView(DetailView):
    template_name = 'Professor/detail_professor.html'
    model = Professor


class ProfessorDeleteView(DeleteView):
    template_name = 'Professor/delete_professor.html'
    model = Professor
    success_url = reverse_lazy('list-of-professor')
