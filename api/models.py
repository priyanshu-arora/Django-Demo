from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.IntegerField(null=False, blank=False, unique=True)