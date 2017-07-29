# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/29 09:39'


from django.views.generic import TemplateView
from django.contrib.auth.models import User

class UserListView(TemplateView):
    template_name = "user/userlist.html"

    def get_context_data(self, **kwargs):
        context=super(UserListView,self).get_context_data(**kwargs)
        context['userlist'] = User.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return super(UserListView,self).get(request,*args,**kwargs)