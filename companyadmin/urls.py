from django.urls import path
from . import views

app_name = 'companyadmin'
urlpatterns = [
    path('home',views.home_page,name='home'),
    path('addemploye',views.addemployee_page,name='addemploye'),
    path('addproject',views.addproject_page,name='addproject'),
    path('addmembers',views.addmembers_page,name='addmembers'),
    path('projectstatus',views.projectstatus_page,name='projectstatus'),
    path('getleader',views.getleader,name='getleader'),
    path('email_exist',views.email_exist,name='email_exist'),
    path('proj_exist',views.proj_exist,name='proj_exist'),
]