from django.db import models
from django.utils import timezone
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()
    marks = models.IntegerField(null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50)


    # Relationship field
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
