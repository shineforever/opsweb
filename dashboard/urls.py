# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/18 10:11'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^test_form/$', views.test_form),

]




