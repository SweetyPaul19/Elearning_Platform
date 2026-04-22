from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Elearningapp.models import *
from django.contrib import messages

def home(request):
    return HttpResponse("hello world")
def master(request):
    return render(request,'master.html')  
def admindashboard(request):
    if request.session.has_key('adminemail'):
        return render(request,'admindashboard.html')
    else:
        messages.success(request,'please login!')
        return redirect('/adminlogin')
def addadmin(request):
    admin=Elearningadmin.objects.all()
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        gender=request.POST['gender']
        file=request.POST['file']
        city=request.POST['city']
        admin=Elearningadmin(name=name,email=email,mobile=mobile,password=password,gender=gender,file=file,city=city)
        admin.save()
        messages.success(request,'added successfully')
        return redirect('/addadmin')
    else:    
        return render(request,'addadmin.html',{'admin':admin})

def edit(request,id):
    admin=Elearningadmin.objects.get(id=id)
    if(request.method=="POST"):
        name=request.POST['name']
        mobile=request.POST['mobile']
        gender=request.POST['gender']
        file=request.FILES['file']
        city=request.POST['city']
        admin.name=name
        admin.mobile=mobile
        admin.gender=gender
        admin.file=file
        admin.city=city
        admin.save()
        messages.success(request,'edited successfull')
        return redirect('/addadmin')
    else:
        return render(request,'edit.html',{'admin':admin})

def delete(request,id): 
    admin=Elearningadmin.objects.get(id=id)  
    admin.delete()  
    return redirect('/addadmin')

def adminlogin(request):
    if request.session.has_key('adminemail'):
        del request.session['adminemail']  #loging out process
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        usercheck=Elearningadmin.objects.filter(email=email,password=password)
        if(usercheck):
            request.session['adminemail']=email
            messages.success(request,'login successfully')
            return redirect('/admindashboard')
        else:
            messages.success(request,'wrong password or username')
            return redirect('/adminlogin')
    else:
        return render(request,'adminlogin.html')

def addcoursetype(request):
    coursetype1=coursetype.objects.all()
    if(request.method=='POST'):
        name=request.POST['name']
        file=request.FILES['file']
        coursetype1=coursetype(name=name,file=file)
        coursetype1.save()
        messages.success(request,'added successfully')
        return redirect('/addcoursetype')
    else:    
        return render(request,'addcoursetype.html',{'coursetype':coursetype1})

def addcoursetype_delete(request,id): 
    coursetype1=coursetype.objects.get(id=id)  
    coursetype1.delete()  
    return redirect('/addcoursetype')

def addcoursetype_edit(request,id):
    coursetype1=coursetype.objects.get(id=id)
    if(request.method=="POST"):
        name=request.POST['name']
        file=request.FILES['file']
        coursetype1.name=name
        coursetype1.file=file
        coursetype1.save()
        messages.success(request,'edited successfull')
        return redirect('/addcoursetype')
    else:
        return render(request,'addcoursetype_edit.html',{'coursetype':coursetype1})

def addcourse(request):
    course1=course.objects.all()
    coursetype1=coursetype.objects.all()
    if(request.method=='POST'):
        coursetypes=request.POST['coursetypes']
        name=request.POST['name']
        price=request.POST['price']
        file=request.FILES['file']
        course1=course(coursetypes=coursetypes,name=name,price=price,file=file)
        course1.save()
        messages.success(request,'added successfully')
        return redirect('/addcourse')
    else:    
        return render(request,'addcourse.html',{'coursetype':coursetype1,'course':course1})

def addcourse_edit(request,id):
    course1=course.objects.get(id=id)
    coursetype1=coursetype.objects.all()
    if(request.method=="POST"):
        coursetypes=request.POST['coursetypes']
        name=request.POST['name']
        price=request.POST['price']
        file=request.FILES['file']
        course1.name=name
        course1.price=price
        course1.file=file
        course1.save()
        messages.success(request,'edited successfull')
        return redirect('/addcourse')
    else:
        return render(request,'addcourse_edit.html',{'coursetype':coursetype1,'course':course1})

def addcourse_delete(request,id): 
    course1=course.objects.get(id=id)  
    course1.delete()  
    return redirect('/addcourse')
def addteachers(request):
    course1=teacher.objects.all()
    if(request.method=='POST'):
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        file=request.FILES['file']
        teacher1=teacher(name=name,phone=phone,email=email,password=password,file=file)
        teacher1.save()
        messages.success(request,'added successfully')
        return redirect('/addteachers')
    else:    
        return render(request,'addteachers.html',{'course':course1})
def addteachers_edit(request,id):
    teacher1=teacher.objects.get(id=id)
    if(request.method=="POST"):
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        file=request.FILES['file']
        teacher1.name=name
        teacher1.phone=phone
        teacher1.email=email
        teacher1.password=password
        teacher1.file=file
        teacher1.save()
        messages.success(request,'edited successfull')
        return redirect('/addteachers')
    else:
        return render(request,'addteachers_edit.html',{'teacheredit':teacher1})   
def addteachers_delete(request,id): 
    teacher1=teacher.objects.get(id=id)  
    teacher1.delete()  
    return redirect('/addteachers')     
def teacherslogin(request): 
    if request.session.has_key('email'):
        del request.session['email']  #loging out process
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        usercheck=teacher.objects.filter(email=email,password=password)
        if(usercheck):
            request.session['email']=email
            messages.success(request,'login successfully')
            return redirect('/teacherdashboard')
        else:
            messages.success(request,'wrong password or username')
            return redirect('/teacherslogin')
    else:
        return render(request,'teacherslogin.html')  
def teacherdashboard(request):
    if request.session.has_key('email'):
        return render(request,'teacherdashboard.html')
    else:
        messages.success(request,'please login!')
        return redirect('/teacherslogin')        
def website_index(request):
    admin=headlines.objects.all()
    Coursetype=coursetype.objects.all()
    course1=course.objects.all()
    return render(request,'website_index.html',{'admin':admin,'coursetype':Coursetype,'course':course1}) 

def addheadlines(request):
    admin=headlines.objects.all()
    if(request.method=='POST'):
        heading1=request.POST['heading1']
        heading2=request.POST['heading2']
        heading3=request.POST['heading3']
        file=request.FILES['file']
        admin=headlines(heading1=heading1,heading2=heading2,heading3=heading3,file=file)
        admin.save()
        messages.success(request,'added successfully')
        return redirect('/addheadlines')
    else:    
        return render(request,'addheadlines.html',{'admin':admin})
def addheadlines_delete(request,id): 
    admin=headlines.objects.get(id=id)  
    admin.delete()  
    return redirect('/addheadlines')        

def about(request):
    return render(request,'about.html')     

def contact(request):    
    return render(request,'contact.html')

def join_now(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        school_college=request.POST['school_college']
        user=elearning_users(name=name,email=email,phone=phone,password=password,school_college=school_college)
        user.save()
        messages.success(request,'registration successfully')
        return redirect('/join_now')
    else:
        return render(request,'join_now.html')    