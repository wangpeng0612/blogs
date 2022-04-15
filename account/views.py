from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_deny, xframe_options_sameorigin

from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile


# def user_login(request):
#     if request.method == "POST":
#         print("hello")
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             cd = login_form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#
#             if user:
#                 login(request, user)
#                 return HttpResponse("登录成功")
#             else:
#                 return HttpResponse("登录失败，请检查用户名和密码")
#         else:
#             return HttpResponse("登录无效")
#
#     if request.method == "GET":
#         print("get")
#         login_form = LoginForm()
#         return render(request, 'account/login.html', {'form': login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        print(user_form.is_valid())
        print(userprofile_form.is_valid())
        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse("对不起，注册失败")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})
