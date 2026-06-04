from django.urls import path
from Elearningapp import views
urlpatterns=[
    path('',views.website_index,name='website_index'),
    path('master',views.master,name='master'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('addadmin',views.addadmin,name='addadmin'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('addcoursetype',views.addcoursetype,name='addcoursetype'),
    path('addcoursetype_edit/<int:id>',views.addcoursetype_edit,name='addcoursetype_edit'),
    path('addcoursetype_delete/<int:id>',views.addcoursetype_delete,name='addcoursetype_delete'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcourse_edit/<int:id>',views.addcourse_edit,name='addcourse_edit'),
    path('addcourse_delete/<int:id>',views.addcourse_delete,name='addcourse_delete'),

    path('addteachers',views.addteachers,name='addteachers'),
    path('addteachers_edit/<int:id>',views.addteachers_edit,name='addteachers_edit'),
    path('addteachers_delete/<int:id>',views.addteachers_delete,name='addteachers_delete'),
    path('teacherslogin',views.teacherslogin,name='teacherslogin'),
    path('teacherdashboard',views.teacherdashboard,name='teacherdashboard'),

    
    path('addheadlines',views.addheadlines,name='addheadlines'),
    path('addheadlines_delete/<int:id>',views.addheadlines_delete,name='addheadlines_delete'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('join_now',views.join_now,name='join_now'),
    path('user_login',views.user_login,name='user_login'),
    path('course_details/<int:id>',views.course_details,name='course_details'),
    path('assigncourse/<int:id>',views.assigncourse,name='assigncourse'),
    path('course_remove/<int:id>',views.course_remove,name='course_remove'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('verify_user_otp',views.verify_user_otp,name='verify_user_otp'),
    path('reset_password',views.reset_password,name='reset_password')
]

