from django.shortcuts import render

# Create your views here.
def tixaction(request):
    return render(request, 'tickets.html')