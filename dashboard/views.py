# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def hello(request):
    """
    测试页面
    :param request: 
    :return: 
    """
    return HttpResponse("hello world!!!")

def login_view(request):
    """
    登录页面
    :param request: 
    :return: 
    """
    if request.method == 'GET':
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        #验证用户名和密码
        user = authenticate(username=username,password=password)

        if user is not None:
            print user
            if user.is_active:
                login(request,user)  #传入的是user对象，而不是username
                return HttpResponse('login success')
            else:
                return HttpResponse('user is block')
        else:
            return HttpResponse('user or password is wrong!')

def logout_view(request):
    """
    账户登出
    :param request: 
    :return: 
    """
    logout(request)
    return HttpResponse('user logout')
