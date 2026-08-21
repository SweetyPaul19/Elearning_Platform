from django.urls import path 
from Elearningapp import views
urlpatterns=[
    path('',views.website_index,name='website_index'),
    path('master',views.master,name='master'),
    path('admin_master',views.admin_master,name='admin_master'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('addadmin',views.addadmin,name='addadmin'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('addcoursetype',views.addcoursetype,name='addcoursetype'),
    path('addcoursetype_edit/<int:id>',views.addcoursetype_edit,name='addcoursetype_edit'),
    path('addcoursetype_delete/<int:id>',views.addcoursetype_delete,name='addcoursetype_delete'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcourse_edit/<int:id>',views.addcourse_edit,name='addcourse_edit'),
    path('addcourse_delete/<int:id>',views.addcourse_delete,name='addcourse_delete'),

    path('addteachers',views.addteachers,name='addteachers'),
    path('addteachers_edit/<int:id>',views.addteachers_edit,name='addteachers_edit'),
    path('addteachers_delete/<int:id>',views.addteachers_delete,name='addteachers_delete'),
    path('teacherdashboard',views.teacherdashboard,name='teacherdashboard'),

    
    path('addheadlines',views.addheadlines,name='addheadlines'),
    path('addheadlines_delete/<int:id>',views.addheadlines_delete,name='addheadlines_delete'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('join_now',views.join_now,name='join_now'),
    path('joining_otp_verification',views.joining_otp_verification,name='joining_otp_verification'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('course_details/<int:id>',views.course_details,name='course_details'),
    path('course_assign/<int:id>',views.course_assign,name='course_assign'), #this is for course assign to teachers 
    path('course_remove/<int:id>',views.course_remove,name='course_remove'),

    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('verify_user_otp',views.verify_user_otp,name='verify_user_otp'),
    path('reset_password',views.reset_password,name='reset_password'),
    path('before_payment/<int:id>',views.before_payment,name='before_payment'),
    path('user_profile_master',views.user_profile_master,name='user_profile_master'),
    path('user_dashboard',views.user_dashboard,name='user_dashboard'),
    path('My_Batch',views.My_Batch,name='My_Batch'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('recorded_lecture',views.recorded_lecture,name='recorded_lecture'),
    path('teachers_login',views.teachers_login,name='teachers_login'),
    path('teachers_master',views.teachers_master,name='teachers_master'),
    path('teacher_logout',views.teacher_logout,name='teacher_logout'),
    path('teacher_my_batch',views.teacher_my_batch,name='teacher_my_batch'),
    path('admin_viewalldetails_teachers',views.admin_viewalldetails_teachers,name='admin_viewalldetails_teachers')
    ]

