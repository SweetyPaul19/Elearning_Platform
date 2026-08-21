from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Elearningapp.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

import random

from django.contrib.auth.models import User

from datetime import datetime, timedelta # Importing datetime and timedelta for handling time-related operations , such as setting OTP expiration time

import random

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from datetime import datetime, timedelta # Importing datetime and timedelta for handling time-related operations , such as setting OTP expiration time 

def home(request):
    return HttpResponse("hello world")
def master(request):
    return render(request,'master.html')  
def admindashboard(request):
    if request.session.has_key('adminemail'):
        eid=request.session['adminemail']# Get the email of the logged-in user from the session
        admin=Elearningadmin.objects.get(email=eid)# Retrieve the admin object based on the email
        stu=elearning_users.objects.count()
        Teacher=teacher.objects.count()
        Course=course.objects.count()
        return render(request,'admindashboard.html', {'admin': admin,'stu':stu,'Teacher':Teacher,'Course':Course})

    else:
        messages.success(request,'please login!')
        return redirect('/adminlogin')
def addadmin(request):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
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
    if request.method == "POST":
        email = request.POST['adminemail']
        password = request.POST['password']

        usercheck = Elearningadmin.objects.filter(
            email=email,
            password=password
        )

        if usercheck.exists():
            request.session['adminemail'] = email
            messages.success(request, 'Login successfully')
            return redirect('/admindashboard')
        else:
            messages.error(request, 'Wrong password or username')
            return redirect('/adminlogin')
    return render(request, 'adminlogin.html')
def admin_logout(request):
    if request.session.has_key('adminemail'):
        del request.session['adminemail']  #loging out process
    messages.success(request,'logout successfully')
    return redirect('/')
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
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])    
    course1=course.objects.all()
    coursetype1=coursetype.objects.all()
    if(request.method=='POST'):
        coursetypes=request.POST['coursetypes']
        name=request.POST['name']
        duration=request.POST['duration']
        language=request.POST['language']
        price=request.POST['price']
        file=request.FILES['file']
        course1=course(coursetypes=coursetypes,name=name,duration=duration,language=language,price=price,file=file)
        course1.save()
        messages.success(request,'added successfully')
        return redirect('/addcourse')
    else:    
        return render(request,'addcourse.html',{'coursetype':coursetype1,'course':course1,'admin':admin})

def addcourse_edit(request,id):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])    
    course1=course.objects.get(id=id)
    coursetype1=coursetype.objects.all()
    if(request.method=="POST"):
        coursetypes=request.POST['coursetypes']
        name=request.POST['name']
        duration=request.POST['duration']
        language=request.POST['language']
        price=request.POST['price']
        file=request.FILES['file']
        Description=request.POST['Description']
        course1.name=name
        course1.duration=duration
        course1.language=language
        course1.price=price
        course1.file=file
        course1.Description=Description
        course1.save()
        messages.success(request,'edited successfull')
        return redirect('/addcourse')
    else:
        return render(request,'addcourse_edit.html',{'coursetype':coursetype1,'course':course1,'admin':admin})

def addcourse_delete(request,id): 
    course1=course.objects.get(id=id)  
    course1.delete()  
    return redirect('/addcourse')
def addteachers(request):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])    
    Teacher=teacher.objects.all()
    course2=course.objects.all()
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
        return render(request,'addteachers.html',{'teacher':Teacher,'courses':course2,'admin':admin})
def addteachers_edit(request,id):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])
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
        return render(request,'addteachers_edit.html',{'teacheredit':teacher1,'admin':admin})   
def addteachers_delete(request,id): 
    teacher1=teacher.objects.get(id=id)  
    teacher1.delete()  
    return redirect('/addteachers')            
def website_index(request):
    ename=None
    user = None
    teacher1=None
    if request.session.has_key('email'):# Check if user is logged in
        eid=request.session['email']# Get the email of the logged-in user from the session 
        role=request.session.get('role')  # Get the role of the logged-in user from the session
        if role == 'student':

            user = elearning_users.objects.filter(
                email=eid
            ).first()

            if user:
                ename = user.name

        elif role == 'teacher':

            teacher1 = teacher.objects.filter(
                email=eid
            ).first()

            if teacher1:
                ename = teacher1.name
    admin=headlines.objects.all()
    Coursetype=coursetype.objects.all()
    course1=course.objects.all()
    return render(request,'website_index.html',{'admin':admin,'coursetype':Coursetype,'course':course1,'ename':ename}) 

def addheadlines(request):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])    
    Admin=headlines.objects.all()
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
        return render(request,'addheadlines.html',{'admin':admin,'Admin':Admin})
def addheadlines_delete(request,id): 
    admin=headlines.objects.get(id=id)  
    admin.delete()  
    return redirect('/addheadlines')        

def about(request):
    ename=None
    if request.session.has_key('email'):# Check if user is logged in
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user= elearning_users.objects.filter(email=eid).first()# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
    return render(request,'about.html',{'ename':ename})     

def contact(request):    
    ename=None
    if request.session.has_key('email'):# Check if user is logged in
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        
    return render(request,'contact.html',{'ename':ename})

def join_now(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        school_college=request.POST['school_college']
        address=request.POST['address']
        # Check if email already exists
        if elearning_users.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("join_now")

        otp = str(random.randint(100000, 999999))

        # Store registration details in session
        request.session['reg_name'] = name
        request.session['reg_email'] = email
        request.session['reg_phone'] = phone
        request.session['reg_password'] = password
        request.session['reg_school'] = school_college
        request.session['reg_address'] = address
        request.session['register_otp'] = otp

        expiry = datetime.now() + timedelta(minutes=2)
        request.session['register_otp_expiry'] = expiry.strftime('%Y-%m-%d %H:%M:%S')# Store the OTP expiry time in session for later verification 

        send_mail(
            "Email Verification OTP",
            f"Welcome to EdunoVa.Verifying email for creating account.\n\nYour OTP is: {otp}\n\nIt is valid for 2 minutes.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False, 
        )

        messages.success(request, "OTP sent to your email.")
        return redirect("joining_otp_verification")
    
    return render(request,'join_now.html')    

def joining_otp_verification(request):
    expiry = request.session.get("register_otp_expiry")
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        saved_otp = request.session.get("register_otp")
        expiry = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")#
        if datetime.now() > expiry:
            messages.error(request, "OTP expired. Please register again.")
            request.session.flush()  # Clear session data
            return redirect("join_now")
        if user_otp == saved_otp:
            # Retrieve registration details from session
            name = request.session.get("reg_name")
            email = request.session.get("reg_email")
            phone = request.session.get("reg_phone")
            password = request.session.get("reg_password")
            school_college = request.session.get("reg_school")
            address=request.session.get("reg_address")
            # Create a new user in the database
            new_user = elearning_users(
                name=name,
                email=email,
                phone=phone,
                password=password,
                school_college=school_college,
                address=address
            )
            new_user.save()

            # Clear session data after successful registration
            request.session.flush()

            messages.success(request, "Registration successful. You can now log in.")
            return redirect("join_now") 
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            request.session.flush()  # Clear session data
            return redirect("join_now")
    return render(request, "joining_otp_verification.html", {"expiry": expiry})        

def user_login(request): 
    if request.session.has_key('email'):
        del request.session['email']  #loging out process
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        usercheck=elearning_users.objects.filter(email=email,password=password).first()
        if(usercheck):
            request.session['email']=email
            request.session['role'] = 'student'
            messages.success(request,'login successfully')
            return redirect('/')
        else:
            messages.success(request,'wrong password or username')
            return redirect('/user_login')
    else:
        return render(request,'user_login.html')

def user_logout(request):
    if request.session.has_key('email'):
        del request.session['email']  #loging out process
    messages.success(request,'logout successfully')
    return redirect('/')

# def courses(request):
#     course1=course.objects.all()
#     return render(request,'courses.html',{'course':course1})        
def course_details(request,id):
    course1=course.objects.get(id=id)
    return render(request,'course_details.html',{'course':course1})

def course_assign(request,id):
    if not request.session.get('adminemail'):
        messages.error(request, 'Please login first')
        return redirect('adminlogin')
    admin=Elearningadmin.objects.get(email=request.session['adminemail'])
    course1=course.objects.all()
    teacher1=teacher.objects.get(id=id)
    course_assign1 = courseassign.objects.filter(teacherid=id)
    if(request.method=="POST"):
        assigncourse=request.POST['assigncourse']
        course_assign1=courseassign(course_assigned=assigncourse,teacherid=teacher1.id)
        course_assign1.save()
        messages.success(request,'assigned successfully')
        return redirect('/addteachers')
    else:
        return render(request,'course_assign.html',{'teachere':teacher1,'courses':course1,'course_assign':course_assign1,'admin':admin}) 
def course_remove(request,id):
    course_assign1=courseassign.objects.get(id=id)  # Get the course assignment object based on the provided id 
    course_assign1.delete()  # Delete the course assignment object from the database
    messages.success(request,'course removed successfully')  # Display a success message to the user
    return redirect('/addteachers')           

def forgot_password(request):
    if(request.method=="POST"):
        email=request.POST['email']
        usercheck=elearning_users.objects.filter(email=email)
        if(usercheck):
            otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
            request.session['reset_otp'] = otp  # Store OTP in session for later verification 
            request.session['reset_email'] = email  # Store email in session for later use in password reset process
            
            expiry_time = datetime.now() + timedelta(minutes=1)# Set OTP expiry time to 1 minute from now 
            request.session['otp_expiry'] = expiry_time.strftime('%Y-%m-%d %H:%M:%S')
            # Send OTP via email
            send_mail( # Subject of the email, message body, sender's email address, recipient list, and fail_silently flag for error handling 
                'Password Reset OTP',
                f'Your OTP for EdunoVa password reset is: {otp}',
                settings.EMAIL_HOST_USER, # Sender email address (configured in settings.py)
                [email], # Recipient email address 
                fail_silently=False, # Raise an exception if email sending fails, allowing for error handling and debugging 
            )

            messages.success(request,'OTP sent to your email') # Display a success message to the user indicating that the OTP has been sent to their email 
            return redirect('/verify_user_otp')
        else:
            messages.success(request,'email not found')
            return redirect('/forgot_password')
    else:
        return render(request,'forgot_password.html')    

def verify_user_otp(request):
    expiry_time = request.session.get('otp_expiry') # Retrieve the OTP expiry time stored in the session during the forgot password process 
    if request.method == "POST":
        user_otp = request.POST.get('otp') # Get the OTP entered by the user from the form 
        saved_otp = request.session.get('reset_otp') # Retrieve the OTP stored in the session during the forgot password process 
        print("User OTP:", user_otp)  # Debugging: Print the OTP entered by the user
        print("Saved OTP:", saved_otp)  # Debugging: Print the OTP stored

       
        expiry_time = datetime.strptime(expiry_time, '%Y-%m-%d %H:%M:%S') # Convert the expiry time string back to a datetime object for comparison 
        if datetime.now() > expiry_time: # Check if the current time has exceeded the OTP expiry time 
            messages.error(request, "OTP expired")
            return redirect('forgot_password')

        if user_otp == saved_otp:
            messages.success(request, "OTP verified")
            return redirect('reset_password')
        else:
            messages.error(request, "Invalid OTP")
        return render(request, 'verify_user_otp.html',{'otp_expiry': expiry_time})
    return render(request, 'verify_user_otp.html')    

def reset_password(request):

    if request.method == "POST":

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:

            email = request.session.get('reset_email')

            print("Session Email:", email)

            if not email:

                messages.error(request, "Session expired")

                return redirect('forgot_password')

            user = elearning_users.objects.filter(email=email).first()

            print("User Object:", user)

            if not user:

                messages.error(request, "User not found")

                return redirect('forgot_password')

            user.password = new_password
            user.save()

            request.session.flush()

            messages.success(request, "Password reset successfully")

            return redirect('user_login')

        else:

            messages.error(request, "Passwords do not match")

    return render(request, 'reset_password.html')    

def before_payment(request,id):
    course1=course.objects.get(id=id) # Get the course object based on the provided id 
    user=elearning_users.objects.all()
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        if(request.method=="POST"):
            user_email=request.POST['email']
            course_taken_date=datetime.now().strftime('%Y-%m-%d')  # Get the current date and time as the course taken date
            my_batch1=my_batch(course_id=id,user_email=user_email,course_taken_date=course_taken_date)# Create a new instance of the my_batch model with the provided course and user details
            my_batch1.save()
            messages.success(request,'batch added successfully')  # Display a success message to the user
            return redirect('/user_dashboard')
        return render(request, 'before_payment.html',{'course': course1,'user': user})
    
    else:  
        return redirect('/user_login')  # Redirect to login page if user is not logged in      
    
def user_profile_master(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        return render(request, 'user_profile_master.html', {'ename':ename, 'user': user})
    else:
        messages.success(request,'please login!')
        return redirect('/user_login')

def user_dashboard(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        return render(request, 'user_dashboard.html', {'ename':ename, 'user': user})
    else:
        messages.success(request,'please login!')
        return redirect('/user_login')


def My_Batch(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        batches=my_batch.objects.filter(user_email=eid)  # Retrieve all batches associated with the logged-in user's email
        course_list=[] # Create an empty list to store course objects corresponding to the user's batches
        for batch in batches:
            try:
                c = course.objects.get(id=int(batch.course_id))
                course_list.append(c)
            except course.DoesNotExist: # Handle the case where the course with the given ID does not exist 
                pass
        return render(request, 'My_Batch.html', {'ename':ename,'my_batches':batches,'courses':course_list, 'user': user})
    else:
        messages.success(request,'please login!')
        return redirect('/user_login')
def update_profile(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        if request.method == "POST":
            print(request.FILES.get('profile_pic'))
            user.name = request.POST.get('name')
            user.phone = request.POST.get('phone')
            user.email = request.POST.get('email')
            user.address = request.POST.get('address')
            user.gender = request.POST.get('gender')
            # Update profile picture only if a new one is selected
            if 'profile_pic' in request.FILES:
                user.img = request.FILES['profile_pic']
            user.save()
            messages.success(request, "Profile updated successfully.")
        return render(request, 'user_my_profile.html', {'ename':ename,'user':user})
    else:
        messages.success(request,'please login!')
        return redirect('/user_login')
def recorded_lecture(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        user=elearning_users.objects.get(email=eid)# Retrieve the user object based on the email
        ename=user.name # Get the name of the logged-in user from the user object 
        batches=my_batch.objects.filter(user_email=eid)  # Retrieve all batches associated with the logged-in user's email
        course_list=[] # Create an empty list to store course objects corresponding to the user's batches
        for batch in batches:
            try:
                c = course.objects.get(id=int(batch.course_id))
                course_list.append(c)
            except course.DoesNotExist: # Handle the case where the course with the given ID does not exist 
                pass
        return render(request, 'recorded_lecture.html', {'ename':ename,'my_batches':batches,'courses':course_list, 'user': user})
    else:
        messages.success(request,'please login!')
        return redirect('/user_login')        
def teachers_login(request): 
    if request.session.has_key('email'):
        del request.session['email']  #loging out process
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        usercheck=teacher.objects.filter(email=email,password=password).first()
        if(usercheck):
            request.session['email']=email
            request.session['role']='teacher'
            messages.success(request,'login successfully')
            return redirect('/teacherdashboard')
        else:
            messages.success(request,'wrong password or username')
            return redirect('/teachers_login')
    else:
        return render(request,'teachers_login.html')        
def teachers_master(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session 
        Teacher=teacher.objects.get(email=eid)# Retrieve the user object based on the email
        ename=Teacher.name # Get the name of the logged-in user from the user object 
        return render(request, 'teachers_master.html', {'ename':ename, 'Teacher': Teacher})
    else:
        messages.success(request,'please login!')
        return redirect('/teachers_login')        
def teacherdashboard(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session
        Teacher=teacher.objects.get(email=eid)# Retrieve the user object based on the email
        return render(request,'teacherdashboard.html',{'Teacher':Teacher})
    else:
        messages.success(request,'please login!')
        return redirect('/teachers_login')         
def teacher_logout(request):
    if request.session.has_key('email'):
        del request.session['email']  #loging out process
    messages.success(request,'logout successfully')
    return redirect('/')
def teacher_my_batch(request):

    if request.session.has_key('email'):

        eid = request.session['email']
        print(eid)
        # Get logged-in teacher
        Teacher = teacher.objects.get(email=eid)
        print(Teacher)
        # Get courses assigned to this teacher
        batches = courseassign.objects.filter(
            teacherid=int(Teacher.id)
        )
        print(batches)
        course_list = []

        for batch in batches:

            try:
                # course_assigned contains course ID as a string
                c = course.objects.get(
                    id=int(batch.course_assigned)
                )

                course_list.append(c)

            except (course.DoesNotExist, ValueError, TypeError):
                pass

        return render(
            request,
            'teacher_my_batch.html',
            {
                'my_batches': batches,
                'courses': course_list,
                'Teacher': Teacher
            }
        )

    else:
        messages.success(request, 'Please login!')
        return redirect('/teachers_login')
def admin_master(request):
    if request.session.has_key('email'):
        eid=request.session['email']# Get the email of the logged-in user from the session
        admin=Elearningadmin.objects.get(email=eid)# Retrieve the user object based on the email
        return render(request,'admin_master.html',{'admin':admin})
    else:
        messages.success(request,'please login!')
        return redirect('/adminlogin')    

def admin_viewalldetails_teachers(request):
    if request.session.has_key('adminemail'):
        eid=request.session['adminemail']# Get the email of the logged-in user from the session
        admin=Elearningadmin.objects.get(email=eid)# Retrieve the user object based on the email
        Teacher=teacher.objects.all()
        return render(request,'admin_viewalldetails_teachers.html',{'admin':admin,'Teacher':Teacher})
    else:
        messages.success(request,'please login!')
        return redirect('/adminlogin')  