from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    