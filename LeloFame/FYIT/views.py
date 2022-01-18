from django.shortcuts import render, redirect
from django.http import HttpResponse
from LeloFame.FYIT.utils import generateuser
from .models import Profile
from django.contrib.auth import authenticate, login, logout
# Create your views here.


#homepage
def index(request):
    return render(request,"index.html")




#login
def signup(request):
    if request.method=="POST":
        id = generateuser()
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj =Profile(id = id, name = name, email_id = email,password = password, credits = 0)
        obj.save()
        render(request,"login.html")
    render(request,"login.html")


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


    


