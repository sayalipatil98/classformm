from django.db import models

# Create your models here.
class Student(models.Model):
    ids=models.IntegerField()
    nm=models.CharField(max_length=100)
    em=models.EmailField()