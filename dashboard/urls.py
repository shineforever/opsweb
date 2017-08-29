# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/18 10:11'

from django.conf.urls import include, url
from . import views
from . import user


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    # url(r'^user/userlist/$', user.UserListView.as_view()),
    # url(r'^hello/$', views.hello),
    # url(r'^logout/$', views.logout_view),
    url(r'^test_form/$', views.test_form),
    url(r'^user/', include([
        # url(r'^userlist/$',user.UserListView.as_view()),  #templateView方式完成
        url(r'^userlist/$',user.UserListView.as_view()),  #listView方式完成
        url(r'^modify_user_status/$',user.ModifyUserStatusView.as_view()),
        url(r'^modifydepartment/$', user.ModifyDepartmentView.as_view()),
        url(r'^modifyphone/$', user.ModifyUserPhoneView.as_view()),
    ]))
]




