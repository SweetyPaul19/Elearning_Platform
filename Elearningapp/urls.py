from django.urls import path
from Elearningapp import views
urlpatterns=[
    path('',views.home,name='home'),
    path('master',views.master,name='master'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('addadmin',views.addadmin,name='addadmin'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('addcoursetype',views.addcoursetype,name='addcoursetype')

]
