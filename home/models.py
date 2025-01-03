from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=122) 
    department = models.CharField(max_length=122, blank=True) 
    email = models.CharField(max_length=40) 
    password = models.CharField(max_length=15)
    date = models.DateField()
    
    def __str__(self):
        return self.name
    

# class Event(models.Model)
#     name = 