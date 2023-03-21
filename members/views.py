from django.shortcuts import render,redirect
from companyadmin.models import Employe
from teamleaders.models import Task

# Create your views here.
def home_page(request):   
    return render(request,'members/mhome.html')
def viewtask_page(request): 
    tasks = Task.objects.filter(employe_id=request.session['employe'])
    return render(request,'members/viewtask.html',{'tasks':tasks})
def profile_page(request):  
    msg='' 
    if request.method=='POST':
        employe = Employe.objects.get(id = request.session['employe'])

        employe_name = request.POST['e_name']
        email_address = request.POST['e_email']
        address = request.POST['e_address']
        phone_number = request.POST['e_number']
        gender = request.POST['e_gender']

        employe.employe_name = employe_name
        employe.email_address = email_address
        employe.address = address
        employe.phone_number = phone_number
        employe.gender = gender
        employe.save()
        msg = 'Profile updated successfully'
    context = {
        'msg':msg
    }  
    return render(request,'members/profile.html',context)
def pass_page(request):   
    return render(request,'members/pass.html')
def task_com(request,tid):
    task=Task.objects.get(id=tid)
    task.status=True
    task.save()
    return redirect('members:viewtask')
def logout(request):
    if 'employe' in request.session:
        del request.session['employe']
    if 'teamleader' in request.session:
        del request.session['teamleader']
    request.session.flush()
    return redirect('common:emplogin')