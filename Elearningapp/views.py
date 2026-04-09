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
    return render(request,'addcoursetype.html')  
