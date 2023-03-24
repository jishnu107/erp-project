from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def auth_employe(func):
    def wrapper(request,*args,**kwargs):
        if 'employe' in request.session:
           
            return func(request,*args,**kwargs)
        else:
             return redirect('common:emplogin')
    return wrapper