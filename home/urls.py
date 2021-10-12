from django.urls import path

from home import views

urlpatterns = [
                path('home/', views.home, name='index'),
                path('list_of_students/', views.details_student, name='all_students'),
               # home/ adresa url accesata din browser,
               # name = index il folosim in fisierul html pentru a ne redirectiona de la o pagina la alta

                path('list_of_teachers/',views.details_teacher, name='all_teachers'),
                path('',views.HomeTemplateView.as_view(),name='home')

]