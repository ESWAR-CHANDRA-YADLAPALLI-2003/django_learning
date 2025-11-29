from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # maybe called 'user' not 'owner'
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_favorite = models.BooleanField(default=False)  # make sure this field exists
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
