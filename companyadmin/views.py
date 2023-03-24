from django.shortcuts import render, redirect
from . models import Employe, Project, AssignProject, CompAdmin
from django.http import JsonResponse
from .auth_admin import auth_admin
from django.contrib import messages

# Create your views here.

@auth_admin
def home_page(request):
    return render(request, 'companyadmin/home.html')

def login_page(request):
    msg = ''
    if request.method == 'POST':
        admin_email = request.POST['a_email']
        admin_pass = request.POST['a_pass']

        try:
            compadmin = CompAdmin.objects.get(
                email_address=admin_email, password=admin_pass)

            request.session['compadmin'] = compadmin.id
            return redirect('companyadmin:addemploye')
        except:
            msg = 'username or password incorrect'
    return render(request, 'companyadmin/login.html', {'msg': msg})

@auth_admin
def addemployee_page(request):
    msg = ''
    if request.method == 'POST':
        e_name = request.POST['e_name']
        e_email = request.POST['e_email']
        e_address = request.POST['e_address']
        e_number = request.POST['e_number']
        e_gender = request.POST['e_gender']
        if not Employe.objects.filter(email_address=e_email).exists():
            new_employe = Employe(employe_name=e_name, email_address=e_email,
                                  address=e_address, phone_number=e_number, gender=e_gender)
            new_employe.save()
            msg="Employe Added"

    return render(request, 'companyadmin/addemploye.html', {'msg': msg})

@auth_admin
def addproject_page(request):
    employes = Employe.objects.filter(is_leader = 'f')
    if request.method == 'POST':
        proj_name = request.POST['p_name']
        team_lead = request.POST['t_lead']

        team_leader = Employe.objects.get(id=team_lead)
        new_project = Project(project_name=proj_name, teamleader=team_leader)
        new_project.save()
        team_leader.is_leader = True
        team_leader.save()
        messages.success(request, 'Project added successfully!')
    return render(request, 'companyadmin/addproject.html', {'employes': employes})

@auth_admin
def addmembers_page(request):
    msg = ''
    msg1=''
    employes = Employe.objects.filter(is_leader=False)
    projects = Project.objects.all()
    if request.method == 'POST':
        project_name = request.POST['proj']
        members = request.POST['memb']
        leader_name = request.POST['c_name']
        if AssignProject.objects.filter(project_id=project_name, employe_id=members).exists():
            msg = 'This member is already assigned to a project'
        else:
            leader = Employe.objects.get(employe_name=leader_name)

            assign_memb = Employe.objects.get(id=members)
            assign_proj = Project.objects.get(id=project_name)
            proj_assign = AssignProject(
                project=assign_proj, employe=assign_memb, team_leader=leader)
            proj_assign.save()
            msg1 = 'Member is assigned to the project'

    context = {
        'employes': employes,
        'project': projects,
        'msg': msg,
        'msg1': msg1
    }
    return render(request, 'companyadmin/addmembers.html', context)

@auth_admin
def projectstatus_page(request):
    projects = Project.objects.values('project_name')

    context = {
        'projects': projects,
    }
    return render(request, 'companyadmin/projectstatus.html', context)


def getleader(request):
    id = request.POST['id']
    product = Project.objects.get(id=id)
    leader = product.teamleader.employe_name
    return JsonResponse({'leader': leader})


def email_exist(request):
    email = request.POST['email']

    status = Employe.objects.filter(email_address=email).exists()

    return JsonResponse({'status': status})

def memb_exist(request):
    member = request.POST['member']

    status = AssignProject.objects.filter(employe_id=member).exists()

    return JsonResponse({'status': status})


def proj_exist(request):
    project = request.POST['name']

    status = Project.objects.filter(project_name=project).exists()

    return JsonResponse({'status': status})


def logout_page(request):
    if 'compadmin' in request.session:
        del request.session['compadmin']
    return redirect('companyadmin:login')
