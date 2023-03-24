from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('home', views.home_page, name='home'),
    path('viewtask', views.viewtask_page, name='viewtask'),
    path('profile', views.profile_page, name='profile'),
    path('pass', views.pass_page, name='pass'),
    path('task_com/<int:tid>', views.task_com, name='task_com'),
    path('logoutemp', views.logout_emp, name='logoutemp'),
]
