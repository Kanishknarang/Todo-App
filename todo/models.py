from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoItem(models.Model):
    content = models.TextField()
    tasktime = models.TimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    