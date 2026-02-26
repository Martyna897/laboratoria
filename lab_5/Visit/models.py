from django.db import models

class Visit(models.Model):
    count = models.IntegerField(default=0)

# Create your models here.
