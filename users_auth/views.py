from django.shortcuts import render
from django.views.generic import TemplateView


class UserInfoView(TemplateView):
    template_name = 'users_auth/info.html'

