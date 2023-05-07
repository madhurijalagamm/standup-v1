from django.shortcuts import render, redirect
from .models import Announcement
from django.contrib import messages


def announcements(request):
    if request.method == 'POST' and request.user.is_superuser:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Announcement.objects.create(title=title, content=content)
        messages.success(request, 'Announcement added successfully')



    announcements = Announcement.objects.order_by('-date')
    context = {'announcements': announcements}
    return render(request, 'announcements.html', context)
