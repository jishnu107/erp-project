from django.shortcuts import render,redirect
from . models import Employe,Project,AssignProject
from django.http import JsonResponse

# Create your views here.
def home_page(request):

    return render(request,'companyadmin/home.html')
def addemployee_page(request):
    msg = ''
    if request.method == 'POST': 
        e_name = request.POST['e_name'] 
        e_email = request.POST['e_email']
        e_address = request.POST['e_address']
        e_number = request.POST['e_number']
        e_gender = request.POST['e_gender']
        if not Employe.objects.filter(email_address=e_email).exists():
            new_employe = Employe(employe_name = e_name , email_address = e_email,address = e_address,phone_number = e_number,gender= e_gender)
            new_employe.save()
        else:
            msg="Email alredy exist"    

    return render(request,'companyadmin/addemploye.html',{'msg':msg})
def addproject_page(request):
    employes = Employe.objects.all()
    if request.method == 'POST': 
        proj_name = request.POST['p_name'] 
        team_lead = request.POST['t_lead']

        team_leader = Employe.objects.get(id = team_lead)
        new_project = Project(project_name = proj_name,teamleader = team_leader)
        new_project.save()
        team_leader.is_leader = True
        team_leader.save()
    return render(request,'companyadmin/addproject.html',{'employes':employes})
def addmembers_page(request):
    msg = ''
    employes =  Employe.objects.filter(is_leader = False)
    projects = Project.objects.all()
    if request.method == 'POST': 
        project_name = request.POST['proj'] 
        members = request.POST['memb']
        leader_name = request.POST['c_name']
        leader = Employe.objects.get(employe_name=leader_name)


        assign_memb = Employe.objects.get(id = members)
        assign_proj = Project.objects.get(id = project_name)
        proj_assign = AssignProject(project = assign_proj,employe = assign_memb,team_leader=leader)
        proj_assign.save()
        msg = 'member added'


    context = {
        'employes':employes,
        'project':projects,
        'msg':msg
    }   
    return render(request,'companyadmin/addmembers.html',context)
def projectstatus_page(request): 
    projects =  Project.objects.all()

    context = {
        'projects':projects,
    }     
    return render(request,'companyadmin/projectstatus.html',context)
def getleader(request):
    id = request.POST['id']
    product =Project.objects.get(id=id)
    leader = product.teamleader.employe_name
    return JsonResponse({'leader':leader})
def email_exist(request):
    email = request.POST['email']

    status = Employe.objects.filter(email_address = email).exists()

    return JsonResponse({'status':status})
def proj_exist(request):
    project = request.POST['name']

    status = Project.objects.filter(project_name = project).exists()

    return JsonResponse({'status':status})
