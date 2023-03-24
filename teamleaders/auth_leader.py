from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def auth_leader(func):
    def wrapper(request,*args,**kwargs):
        if 'teamleader' in request.session:
           
            return func(request,*args,**kwargs)
        else:
             return redirect('common:login')
    return wrapper