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

class coursetype(models.Model):
    name=models.CharField(max_length=50)
    file=models.ImageField(upload_to='image',default='')
    def _str_(self):
        return self.name

class course(models.Model):
    coursetypes=models.CharField(max_length=50,default='')
    name=models.CharField(max_length=50)
    file=models.ImageField(upload_to='image',default='')
    price=models.IntegerField(default=0)
    def _str_(self):
        return self.name
class teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=50)   
    file=models.ImageField(upload_to='image',default='')    
    def _str_(self):
        return self.name        

class headlines(models.Model):
    heading1=models.CharField(max_length=50)
    heading2=models.CharField(max_length=50)
    heading3=models.CharField(max_length=50)
    file=models.ImageField(upload_to='image',default='')    
    def _str_(self):
        return self.heading1        

class elearning_users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(default=0)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)   
    school_college=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    def _str_(self):
        return self.name