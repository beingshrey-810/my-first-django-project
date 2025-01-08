from django.db import models
from datetime import date

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=122) 
    description = models.TextField()
    date = models.DateField(default=date.today, null=True, blank=True)
    author = models.CharField(max_length=122)
    blog_image = models.ImageField(null=True,blank=True, upload_to= "images/" )

    
    def __str__(self):
        return self.title
    

