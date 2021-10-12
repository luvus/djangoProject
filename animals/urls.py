from django.urls import path

from animals import views

urlpatterns = [
    path('create_new_animal/', views.AnimalsCreateView.as_view(), name='create-new-animal')
]
