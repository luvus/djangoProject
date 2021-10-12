from django.db import models


class Professor(models.Model):
    first_name_professor = models.CharField(max_length=30)
    last_name_professor = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    date_of_employment = models.DateField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=1)

