from django.db import models
from django.contrib.auth.models import User

class AddUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    user_unique_id = models.CharField(max_length=6, unique=True)


