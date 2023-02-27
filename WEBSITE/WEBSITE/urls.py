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
from django.urls import path
from home.views import homeaction
from signup.views import signaction
from login.views import loginaction
from jokes.views import jokeaction
from jokes.views import joke_list
from performers.views import performeraction
from jokes.views import create_joke
from signup.views import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signaction),
    path('jokes/', create_joke),
    path('signup/', create_user),
    path('login/', loginaction),
    # path('jokes/', jokeaction),
    path('seejokes/', joke_list),
    path('performers/', performeraction),
    path('welcome/', homeaction),


]
