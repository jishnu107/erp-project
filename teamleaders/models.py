from django.db import models
from companyadmin.models import Employe

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=110)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='assigned_tasks')
    team_leader = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='added_tasks')
    expected_date = models.CharField(max_length=20)
    status = models.BooleanField(default=False)