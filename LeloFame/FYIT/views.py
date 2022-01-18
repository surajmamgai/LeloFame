from django.shortcuts import render, redirect
from django.http import HttpResponse
from FYIT import utils
from .models import Profile
from django.contrib.auth import authenticate, login, logout
# Create your views here.


#homepage
def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")
    
    

#login
def signup(request):
    if request.method=="POST":
        id = utils.generateuser()
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj =Profile(id = id, first_name=first_name, last_name=last_name, email = email,password = password, credits = 0)
        obj.save()
        return render(request,"login.html")
    return render(request,"login.html")


#login
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        id = request.POST.get('id')
        password = request.POST.get('password')
        user = authenticate(id=id, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    else:
        return render(request,'login.html')
    return render(request,'login.html')


#logout
def logout(request):
    logout(request)
    return redirect('login')

