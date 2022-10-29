from django.db import models


class ToDoList(models.Model):
    # id = models.IntegerField()
    to_do = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    until_date = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)