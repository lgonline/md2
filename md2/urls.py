"""md2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from vulmgmt import views as vulmgmt_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',vulmgmt_views.vul_index),
    url(r'^login_action/$',vulmgmt_views.login_action),
    url(r'^vulmgmt_main/$',vulmgmt_views.vulmgmt_main),
    url(r'^vul_track_main/$',vulmgmt_views.vul_track_main),
    url(r'^vul_issue_main/$',vulmgmt_views.vul_issue_main),
]