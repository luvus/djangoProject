from django.db import models


class Animals(models.Model):
    name_of_animal = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    date_of_vaccination = models.DateField()
    email_of_owner = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=1)


