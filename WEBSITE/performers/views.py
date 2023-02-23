from django.shortcuts import render

# Create your views here.
def performeraction(request):
    return render(request,'performers.html')
