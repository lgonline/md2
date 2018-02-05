from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Vulmgmt_Event

# Create your views here.

def vul_index(request):
    return render(request,'vulmgmt_web/login.html')

def login_action(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        request.session['user'] = username
        response  = HttpResponseRedirect('/vulmgmt_main/')
        return response
    else:
        return render(request,'vulmgmt_web/login.html',{'error':'username or password is wrong!'})

@login_required
def vulmgmt_main(request):
    user = request.POST.get('user','')
    post_list = Vulmgmt_Event.objects.all()
    return render(request,'vulmgmt_web/vulmgmt_main.html',{'user':user,'post_list':post_list})

@login_required
def vul_track_main(request):
    user = request.POST.get('user','')
    return render(request,'vulmgmt_web/vulmgmt_vul_tracking.html',{'user':user})

@login_required
def vul_issue_main(request):
    user = request.POST.get('user','')
    return render(request,'vulmgmt_web/vulmgmt_issue_main.html',{'user':user})

@login_required
def vul_dashboard(request):
    user = request.POST.get('user','')
    return render(request)


