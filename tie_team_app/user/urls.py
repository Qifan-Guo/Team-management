"""Defines URL patterns for users"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'user'
urlpatterns = [
    #Home Page
    path('',views.index,name='index'),
    #Login Page
    path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
    #Logout Page
    path('logout/',views.logout_view,name='logout'),
    #Team Stats Page
    path('teamstats/',views.teamstats_view,name='teamstats'),
    #My Profile Page
    path('myprofile/',views.myprofile_view,name='myprofile'),
]