from django.db import models

# Create your models here.
class Elearningadmin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField(default=0)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    file=models.ImageField(upload_to='image',default='')
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.name
