# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

from django.views.generic import View

from django.contrib.auth.models import User



# Create your views here.

def hello(request):
    """
    测试页面
    :param request: 
    :return: 
    """
    return HttpResponse("hello world!!!")


class IndexView(View):
    def get(self, request):
        # template_name = "public/index.html"
        return render(request, 'public/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', {"title": "reboot 运维平台"})

    def post(self, request):
        res = {"status": 0}
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # 验证用户名和密码
        user = authenticate(username=username, password=password)

        if user is not None:
            print user
            print password
            if user.is_active:
                login(request, user)  # 传入的是user对象，而不是username
                res['next_url'] = "/"
                # return HttpResponse('login success')
            else:
                res['status'] = 1
                res['errmsg'] = "user is block"

                # return HttpResponse('user is block')
        else:
            res['status'] = 2
            res['errmsg'] = "user or password is wrong!"
        return JsonResponse(res, safe=True)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('user logout')





        # def login_view(request):
        #     """
        #     登录页面
        #     :param request:
        #     :return:
        #     """
        #     if request.method == 'GET':
        #         return render(request, 'user/login.html', {"title": "reboot 运维平台"})
        #     if request.method == 'POST':
        #         res = {"status": 0}
        #         username = request.POST.get('username',None)
        #         password = request.POST.get('password',None)
        #
        #         #验证用户名和密码
        #         user = authenticate(username=username,password=password)
        #
        #         if user is not None:
        #             print user
        #             print password
        #             if user.is_active:
        #                 login(request,user)  #传入的是user对象，而不是username
        #                 res['next_url']="/"
        #                 # return HttpResponse('login success')
        #             else:
        #                 res['status'] = 1
        #                 res['errmsg'] = "user is block"
        #
        #                 # return HttpResponse('user is block')
        #         else:
        #             res['status'] = 2
        #             res['errmsg'] = "user or password is wrong!"
        #         return JsonResponse(res, safe=True)
        # return HttpResponse('user or password is wrong!')


# def logout_view(request):
#     """
#     账户登出
#     :param request:
#     :return:
#     """
#     logout(request)
#     return HttpResponse('user logout')



def test_form(request):
    """
    form 测试
    :param request: 
    :return: 
    """

    # return HttpResponse('form 测试')
    if request.method == 'GET':
        return render(request, 'test/test_form.html')
    elif request.method == 'POST':
        print request.POST
        print request.POST.lists()  # list形式表现
        print request.POST.dict()  # 获取字典形式，value只显示一个值，
        username = request.POST.get('username', None)
        fav = request.POST.getlist('fav', None)  # getlist方法获取一个list，如果这个地方用get，只能获取列表的最后一个元素；
        print username
        print fav

        return HttpResponse('OK')
