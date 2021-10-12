from django.urls import path

from student import views

urlpatterns = [
    path('create_new_student/', views.StudentCreateView.as_view(), name='create-new-student'),
    path('all_students/', views.StudentListView.as_view(), name='list-of-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name='detail-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student')
]
