from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Types(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        TEACHER = "TEACHER" , "Teacher"
        STUDENT = "STUDENT" , "Student"

    type = models.CharField(choices = Types.choices, max_length=20,default = Types.STUDENT)

    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True,max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
