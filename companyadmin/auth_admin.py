from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def auth_admin(func):
    def wrapper(request,*args,**kwargs):
        if 'compadmin' in request.session: 
           
            return func(request,*args,**kwargs)
        else:
             return redirect('companyadmin:login')
    return wrapper