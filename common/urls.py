from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('login',views.login_page,name='login'),
    path('emplogin',views.emplogin_page,name='emplogin'),
]