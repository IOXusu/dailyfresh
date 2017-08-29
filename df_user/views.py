# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from models import *
from hashlib import sha1


# Create your views here.
def register(request):
    return render(request, 'df_user/register.html',{'title': "天天生鲜-注册"})


def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否一致
    if upwd != ucpwd:
        return redirect('/user/register/')

    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwdHex = s1.hexdigest()

    # 创建user对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwdHex
    user.uemail = uemail
    user.save()
    # 注册成功后转到登录界面
    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    return render(request, 'df_user/login.html',{'title': "天天生鲜-登录"})
