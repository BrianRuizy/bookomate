from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/login/', views.MyLoginView.as_view(), name='account_login'),
    path('accounts/logout/', views.MyLogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', views.MySignupView.as_view(), name='account_signup'),
    path('accounts/password_reset/', views.MyPasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/', include('allauth.urls')),
]
