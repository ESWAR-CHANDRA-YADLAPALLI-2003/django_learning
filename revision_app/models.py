from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    joined_date = models.DateField()

    def __str__(self):
        return self.name