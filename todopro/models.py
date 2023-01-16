from django.db import models

# Create your models here.


class Todos(models.Model):
    todo = models.TextField()
    time = models.TextField()
    status = models.BooleanField(default=False)
