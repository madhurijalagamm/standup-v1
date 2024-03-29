from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm, EditProfileFormStaff
from admin_dashboard.models import Announcement

# Create your views here.
def homeaction(request):
    allannouncements = Announcement.objects.order_by('-date')
    announcements = []
    for i in range(0, len(allannouncements)):
      if i == 0:
        announcements.append(allannouncements[i])
    context = {'announcements': announcements}
    return render(request, 'home.html', context)

def login_user (request):
  if request.method == 'POST': #if someone fills out form , Post it 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:# if user exist
      login(request, user)
      messages.success(request,('Youre logged in'))

      return redirect('home') #routes to 'home' on successful login  
    else:
      messages.success(request,('Error logging in'))
      return redirect('login') #re routes to login page upon unsucessful login
  else:
    return render(request, 'login.html', {})

def logout_user(request):
  logout(request)
  messages.success(request,('Youre now logged out'))
  return redirect('home')

def register_user(request):
  if request.method =='POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request,user)
      messages.success(request, ('Youre now registered'))
      return redirect('home')
  else: 
    form = SignUpForm() 

  context = {'form': form}
  return render(request, 'register.html', context)

def edit_profile(request):
  if request.method =='POST':
    form = EditProfileForm(request.POST, instance= request.user)
    if form.is_valid():
      form.save()
      messages.success(request, ('You have edited your profile'))
      return redirect('home')
  else:     #passes in user information 
    form = EditProfileForm(instance= request.user) 

  context = {'form': form}
  return render(request, 'edit_profile.html', context)
  #return render(request, 'authenticate/edit_profile.html',{})
  
  
  
  
def edit_profile_staff(request):
  if request.method =='POST':
    form = EditProfileFormStaff(request.POST, instance= request.user)
    if form.is_valid():
      form.save()
      messages.success(request, ('You have edited your profile'))
      return redirect('home')
  else:     #passes in user information 
    form = EditProfileFormStaff(instance= request.user) 

  context = {'form': form}
  return render(request, 'edit_profile2.html', context)
  #return render(request, 'authenticate/edit_profile.html',{})
  
  
  
  
def profile(request):
  return render(request, 'profile.html', {})



def change_password(request):
  if request.method =='POST':
    form = PasswordChangeForm(data=request.POST, user= request.user)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, ('You have edited your password'))
      return redirect('home')
  else:     #passes in user information 
    form = PasswordChangeForm(user= request.user) 

  context = {'form': form}
  return render(request, 'change_password.html', context)