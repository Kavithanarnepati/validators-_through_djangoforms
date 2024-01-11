from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    email=models.EmailField()
    renter_email=models.EmailField()