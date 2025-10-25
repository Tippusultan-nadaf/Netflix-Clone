from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    date=models.DateField()
    
    def __str__(self):
        return self.name