from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users_auth.forms import SignInForm


class UserInfoView(TemplateView):
    template_name = 'users_auth/info.html'


class SignInView(FormView):
    template_name = 'users_auth/sign_in.html'
    form_class = SignInForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data['username']
        psw = form.cleaned_data['password']
        user = authenticate(username=name, password=psw)
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, 'You signed in successfull!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Errors during login!')
        return super().form_invalid(form)