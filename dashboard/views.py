#! coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    """
    测试页面
    :param request: 
    :return: 
    """
    return HttpResponse("hello world!!!")