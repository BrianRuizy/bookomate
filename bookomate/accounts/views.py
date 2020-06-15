from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView, LogoutView, PasswordResetView


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class MyLoginView(LoginView):
    template_name = 'allauth/login.html'


class MyLogoutView(LogoutView):
    template_name = 'allauth/logout.html'


class MySignupView(SignupView):
    template_name = 'allauth/signup.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'allauth/password_reset.html'

