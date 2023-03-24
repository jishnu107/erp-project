from django.db import models

# Create your models here.
class CompAdmin(models.Model):
    email_address = models.CharField(max_length=30)
    password =  models.CharField(max_length=30)
class Employe(models.Model):
    employe_name = models.CharField(max_length=20)
    email_address = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=50)
    is_leader = models.BooleanField(default=False)
class Project(models.Model):
    project_name = models.CharField(max_length=110)
    teamleader = models.ForeignKey(Employe, on_delete=models.CASCADE)
class AssignProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='assigned_memb')
    team_leader = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='leader')







    