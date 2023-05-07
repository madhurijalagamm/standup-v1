from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})


# Create your views here.
def performeraction(request):
    return render(request,'performers.html')
