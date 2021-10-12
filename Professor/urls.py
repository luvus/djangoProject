from django.urls import path
from Professor import views

urlpatterns = [
    path('create_new_professor/', views.ProfessorCreateView.as_view(), name='create-new-professor'),
    path('all_professors/', views.ProfessorListView.as_view(), name='list-of-professor'),
    path('update_professor/<int:pk>/', views.ProfessorUpdateView.as_view(), name='update-professor'),
    path('detail_professor/<int:pk>/', views.ProfessorDetailView.as_view(), name='detail-professor'),
    path('delete_professor/<int:pk>/', views.ProfessorDeleteView.as_view(), name='delete-professor')
    ]
