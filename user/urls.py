from django.urls import path
from user import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-new-user'),

]
