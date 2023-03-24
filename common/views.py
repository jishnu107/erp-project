from django.shortcuts import render, redirect
from companyadmin.models import Employe
from django.http import JsonResponse

# Create your views here.


def login_page(request):
    custmsg = ''
    if request.method == 'POST':
        emp_email = request.POST['e_email']
        emp_num = request.POST['e_num']

        try:
            teamleader = Employe.objects.get(
                email_address=emp_email, phone_number=emp_num, is_leader=True)

            request.session['teamleader'] = teamleader.id
            return redirect('teamleaders:viewemp')
        except:
            custmsg = 'username or password incorrect'
    return render(request, 'common/login.html', {'msg': custmsg})


def emplogin_page(request):
    custmsg = ''
    if request.method == 'POST':
        emp_email = request.POST['e_email']
        emp_num = request.POST['e_num']

        try:
            employe = Employe.objects.get(
                email_address=emp_email, phone_number=emp_num, is_leader=False)

            request.session['employe'] = employe.id
            return redirect('members:viewtask')
        except:
            custmsg = 'username or password incorrect'

    return render(request, 'common/emplogin.html', {'msg': custmsg})
