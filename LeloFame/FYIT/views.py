from django.shortcuts import render, redirect
from django.http import HttpResponse
from FYIT import utils
from .models import Profile, CreditLog
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
        password1 = request.POST.ge('confirmpassword')
        if(password1!=password):
            p = "Password and Confirm Password doesn't matched!"
            return render(request,"signup.html",{p})

        obj =Profile(id = id, first_name=first_name, last_name=last_name, email = email,password = password, credits = 0)
        obj.save()
        return render(request,"login.html")
    return render(request,"signup.html")
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
    return HttpResponse('please enter valid detail')


#logout
def logout(request):
    logout(request)
    return redirect('login')


#credit log

def credit_view(request):
    if request.method=='POST':
        id = request.user.username
        id = Profile.objects.get(id=id)
        credit_spend = request.POST.get('credit_spend')
        platform = request.POST.get('platform')
        type = request.POST.get('type')
        user_id = request.POST.get('user_id')
        flag = utils.left_credit(request.user.username,credit_spend)
        if flag==-1:
            return render(request,'dashboard.html',{'mess':"Not enough amount"})
        else:
            obj = CreditLog(idd=id,credit_spend=credit_spend,platform=platform,type=type,user_id=user_id,credit_left=flag)
            obj.save()
        return redirect('/dashboard')
    return redirect('/dashboard')

def mail(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        utils.send_mail_function(name,email,subject,message)
        return redirect('/')
    return redirect('/')