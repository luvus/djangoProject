
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserForm
from user.models import ExtendUser


class UserCreateView(CreateView):
    template_name = 'user/create_user.html'
    model = ExtendUser
    success_url = reverse_lazy('create-new-user')
    form_class = UserForm
# Create your views here.
