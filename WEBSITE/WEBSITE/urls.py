"""WEBSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from home.views import homeaction
from jokess.views import jokeaction
from jokess.views import joke_list
from performers.views import performeraction
from jokess.views import create_joke
from jokess.views import joke_slugs
from authentication.views import *
from tickets.views import tixaction
from jokess.views import random_word
from admin_dashboard.views import announcements
from performers.views import send_message


# from signup.views import create_user
# from home.views import testaction
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seejokes/', joke_list, name='seejokes'),
    path('performers/', performeraction, name ='performers'),
    path('', homeaction, name='home'),
    # path('', include('authentication.urls')),
    path('login/',login_user, name ='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', register_user, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_profile2/', edit_profile_staff, name='edit_profile2'),
    path('change_password/', change_password, name='change_password'),
    path('profile/', profile, name='profile'),
    # path('<slug:slug>/', joke_slugs, name='joke'),
    # path("", include("jokess.urls")),
    path('tickets/', tixaction, name='tickets'),
    path('seejokes/', random_word),
    path('admin-dashboard/', announcements, name = 'admin-dashboard'),
    path('send-message/', send_message, name='send_message'),
    # path('tickets/', tixaction, name='tickets'),


    







]
