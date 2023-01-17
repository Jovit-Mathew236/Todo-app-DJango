from django.db import models

# Create your models here.


class Todos(models.Model):
    user_id = models.IntegerField()
    todo = models.TextField()
    # day = models.TextField()
    time = models.TextField()
    status = models.BooleanField(default=False)
