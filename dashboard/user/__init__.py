# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/29 09:39'


from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage

from django.http import HttpResponse, JsonResponse

class UserListView(TemplateView):
    template_name = "user/userlist.html"

    before_index = 6
    after_index = 5

    def get_context_data(self, **kwargs):
        context=super(UserListView,self).get_context_data(**kwargs)
        # context['userlist'] = User.objects.all()
        userlist = User.objects.all()
        paginator = Paginator(userlist,10)  #每页显示条目数
        page = self.request.GET.get('page',1)  #获取当前页面的页码数
        try:
            page_obj = paginator.page(page)  #当前页面的数据
        except EmptyPage:
            page_obj = paginator.page(1)
        context['page_obj'] = page_obj

        # print page_obj.paginator.num_pages
        start_index = page_obj.number - self.before_index   #当前页面减去前面的索引
        if start_index < 0:
            start_index = 0
        # print page_obj.paginator.page_range
        context['page_range'] = page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]
        return context

    def get(self, request, *args, **kwargs):
        return super(UserListView,self).get(request,*args,**kwargs)


class ModifyUserStatusView(View):
    """
    修改服务器的状态
    """
    def post(self,request):
        res = {'status':0} #默认为成功
        user_id = request.POST.get('user_id', None)
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
        except user.DoesNotExist:
            res['status'] = 1
            res['errmsg'] = '用户不存在！'

        return JsonResponse(res,safe=True)
    def get(self,request):
        return HttpResponse('OK')