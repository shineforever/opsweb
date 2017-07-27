# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
        ret = {"status": 0}
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        #验证用户名和密码
        user = authenticate(username=username,password=password)

        if user is not None:
            print user
            if user.is_active:
                login(request,user)  #传入的是user对象，而不是username

                # return HttpResponse('login success')
            else:
                ret['status'] = 1
                ret['errmsg'] = "user is block"

                # return HttpResponse('user is block')
        else:
            ret['status'] = 2
            ret['errmsg'] = "user or password is wrong!"
        return JsonResponse(ret, safe=True)
            # return HttpResponse('user or password is wrong!')

def logout_view(request):
    """
    账户登出
    :param request: 
    :return: 
    """
    logout(request)
    return HttpResponse('user logout')


def test_form(request):
    """
    form 测试
    :param request: 
    :return: 
    """

    # return HttpResponse('form 测试')
    if request.method == 'GET':
        return render(request,'test/test_form.html')
    elif request.method == 'POST':
        print request.POST
        print request.POST.lists()   #list形式表现
        print request.POST.dict()   #获取字典形式，value只显示一个值，
        username = request.POST.get('username',None)
        fav = request.POST.getlist('fav',None)   #getlist方法获取一个list，如果这个地方用get，只能获取列表的最后一个元素；
        print username
        print fav

        return HttpResponse('OK')
