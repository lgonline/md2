from django.contrib import admin
from .models import Vulmgmt_Event,Vul_Status,Vul_Level
# Register your models here.

admin.site.register(Vul_Level)
admin.site.register(Vul_Status)
admin.site.register(Vulmgmt_Event)
