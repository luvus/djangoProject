from django.contrib.auth.models import User
from django.db import models


class ExtendUser(User):
    age = models.IntegerField()
    date_of_birth = models.DateField()
    county = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name
