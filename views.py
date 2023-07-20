from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .models import registration


def welcome(request):
   
   #return HttpResponse("welcome to python")
    return render(request,'welcome.html')
    

def Aboutus(request):
     #return HttpResponse("About us")
    return render(request,'Aboutus.html')






def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        interns=request.POST.get('interns')

        return redirect('welcome')  # Replace 'welcome' with the URL name of the welcome page

    return render(request, 'register.html')  # Replace 'register.html' with the actual template name
