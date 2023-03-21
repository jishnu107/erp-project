from django.urls import path
from . import views

app_name = 'teamleaders'
urlpatterns = [
    path('home',views.home_page,name='home'),
    path('addtask',views.addtask_page,name='addtask'),
    path('pass',views.pass_page,name='pass'),
    path('profile',views.profile_page,name='profile'),
    path('taskdetails',views.taskdetails_page,name='taskdetails'),
    path('viewemp',views.viewemp_page,name='viewemp'),
    path('delete/<int:tid>',views.delete_task,name='delete'),
    path('deleteemp/<int:eid>',views.delete_emp,name='deleteemp'),
    path('mail_exist',views.mail_exist,name='mail_exist'),
    path('task_exist',views.task_exist,name='task_exist'),
    path('logout',views.logout_page,name='logout'),

]