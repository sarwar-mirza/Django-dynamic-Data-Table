from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    info = models.CharField(max_length=255)
    course = models.CharField(max_length=70)