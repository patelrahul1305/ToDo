from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class ToDo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    completed_at = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('todo_home')
