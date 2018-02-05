#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: view.py
@time: 2017/12/27 17:26
"""

# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse("Hello World!!!")
    context = {}
    context['hello'] = 'Hello, Mr. Ethan'
    return render(request,'hello.html',context)