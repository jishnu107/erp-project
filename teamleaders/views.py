from django.shortcuts import render, redirect
from companyadmin.models import Employe, AssignProject
from teamleaders.models import Task
from django.http import JsonResponse
from .auth_leader import auth_leader


# Create your views here.
@auth_leader
def home_page(request):
    return render(request, 'teamleaders/home.html')

@auth_leader
def addtask_page(request):
    msg = ''
    team_leader = request.session.get('teamleader')
    employes = AssignProject.objects.filter(team_leader_id=team_leader)
    if request.method == 'POST':
        task_name = request.POST['taskname']
        members = request.POST['members']
        expected_date = request.POST['date']
        team_leader_id = request.session.get('teamleader')
        teamleader = Employe.objects.get(id=team_leader_id)

        memb = Employe.objects.get(id=members)
        task_assign = Task(task_name=task_name, employe=memb,
                           expected_date=expected_date, team_leader=teamleader)
        task_assign.save()
        msg = 'Task Added'

    context = {
        'employes': employes,
        'msg': msg
    }
    return render(request, 'teamleaders/addtask.html', context)

@auth_leader
def pass_page(request):
    return render(request, 'teamleaders/pass.html')

@auth_leader
def profile_page(request):
    msg = ''
    msg1 = ''
    if request.method == 'POST':
        employe = Employe.objects.get(id=request.session.get('teamleader'))

        employe_name = request.POST['e_name']
        email_address = request.POST['e_email']
        address = request.POST['e_address']
        phone_number = request.POST['e_number']
        gender = request.POST['e_gender']
        if not Employe.objects.filter(email_address=email_address).exists():
            employe.employe_name = employe_name
            employe.email_address = email_address
            employe.address = address
            employe.phone_number = phone_number
            employe.gender = gender
            employe.save()
            msg1 = 'Profile updated successfully'
        else:
            msg = 'Email Already Exist'
    context = {
        'msg': msg,
        'msg1': msg1,

    }
    return render(request, 'teamleaders/profile.html', context)

@auth_leader
def taskdetails_page(request):
    tasks = Task.objects.filter(team_leader=request.session.get('teamleader'))
    context = {
        'tasks': tasks
    }
    return render(request, 'teamleaders/taskdetails.html', context)

@auth_leader
def viewemp_page(request):
    team_leader = request.session.get('teamleader')
    employes = AssignProject.objects.filter(team_leader_id=team_leader)
    context = {
        'employes': employes
    }
    return render(request, 'teamleaders/viewemp.html', context)


def delete_task(request, tid):
    task_list = Task.objects.get(id=tid)
    task_list.delete()
    return redirect('teamleaders:taskdetails')


def delete_emp(request, eid):
    employe_list = AssignProject.objects.get(
        employe=eid, team_leader=request.session.get('teamleader'))
    employe_list.delete()
    return redirect('teamleaders:viewemp')


def logout_page(request):
    if 'teamleader' in request.session:
        del request.session['teamleader']
    return redirect('common:login')


def mail_exist(request):
    email = request.POST['email']
    status = Employe.objects.filter(email_address=email).exists()
    return JsonResponse({'status': status})
