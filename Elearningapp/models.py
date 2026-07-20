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
    duration=models.CharField(max_length=50,default='')
    language=models.CharField(max_length=50,default='')
<<<<<<< HEAD
    description=models.CharField(max_length=100,default='')
=======
    Description=models.CharField(max_length=100,default='')
>>>>>>> 661d7ac0f766727dedddc654a88d43c7c3c1fae9
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
    confirm_password=models.CharField(max_length=50,default='')   
    school_college=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=100,default='')
    def _str_(self):
        return self.name
<<<<<<< HEAD
class courseassign(models.Model):
    course_assigned=models.CharField(max_length=50,default='')
    teacherid=models.CharField(max_length=50,default='')  
    def _str_(self):
        return self.course_assigned      
=======

 

class assignedcourse(models.Model):
    course_id=models.CharField(max_length=50,default='')
    teacher_id=models.CharField(max_length=50,default='') 
    teacher_name=models.CharField(max_length=50,default='')
    course_name=models.CharField(max_length=50,default='') 
    def _str_(self):
        return self.assignedcourse    
>>>>>>> 661d7ac0f766727dedddc654a88d43c7c3c1fae9
