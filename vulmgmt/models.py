from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.

class Vul_Level(models.Model):
    level_name = models.CharField(max_length=5)

    def __str__(self):
        return self.level_name

class Vul_Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Vulmgmt_Event(models.Model):
    project_id = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    vul_desc = models.TextField()
    vul_level = models.ForeignKey(Vul_Level,on_delete=models.CASCADE)
    vul_dept = models.CharField(max_length=100)
    vul_responser = models.CharField(max_length=24)
    vul_tracker = models.CharField(max_length=24)
    vul_status = models.ForeignKey(Vul_Status,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField()
    closed_time = models.DateTimeField()
    remark = models.CharField(max_length=200)

    def __str__(self):
        return self.vul_desc

    def get_absolute_url(self):
        return reverse('vulmgmt:')


class Schedule_Task(models.Model):
    project_name = models.CharField(max_length=100)
    project_dept = models.CharField(max_length=200)
    project_owner = models.CharField(max_length=100)
    project_status = models.ForeignKey(Vul_Status,on_delete=models.CASCADE)
    submited_time = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name