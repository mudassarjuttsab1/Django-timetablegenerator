from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, unique=True,null=False, on_delete=models.CASCADE)