from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from users_auth.forms import SignInForm


class UserInfoView(TemplateView):
    template_name = 'users_auth/info.html'


class SignInView(FormView):
    template_name = 'users_auth/sign_in.html'
    form_class = SignInForm
    success_url = settings.LOGIN_REDIRECT_URL

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


class SignOutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        messages.add_message(self.request, messages.INFO, 'You signed out!')
        return settings.LOGOUT_REDIRECT_URL
