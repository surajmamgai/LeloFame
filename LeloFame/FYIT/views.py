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
        id = (utils.generateuser())
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        obj =Profile.objects.create_user(username = id, first_name=first_name, last_name=last_name, email = email,password = password, credits = 0)
        password1 = request.POST.get('confirmpassword')
        if(password1!=password):
            p = "Password and Confirm Password doesn't matched!"
            return render(request,"signup.html",{'p':p})

        # obj =Profile(id = id, first_name=first_name, last_name=last_name, email = email,password = password, credits = 0)
        obj.save()
        return render(request,"login.html")
    return render(request,"signup.html")


#login
def loginn(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    if request.method=="POST":
        username = request.POST.get('id')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username, password=password)
        obj = Profile.objects.filter(username=username,password=password).count()
        print(obj)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
        else:
            return HttpResponse('please enter valid detail')
    return render(request,'login.html')


#logout
def logoutt(request):
    logout(request)
    return redirect('login')


#credit log

def credit_view(request):
    if request.method=='POST':
        id = request.user.username
        id = Profile.objects.get(username=id)
        credit_spend = request.POST.get('credit_spend')
        platform = request.POST.get('platform')
        type = request.POST.get('type')
        user_id = request.POST.get('user_id')
        flag = utils.left_credit(request.user.username,credit_spend)
        if flag==-1:
            return render(request,'dashboard.html',{'mess':"Not enough amount"})
        else:
            obj = CreditLog(username=id,credit_spend=credit_spend,platform=platform,type=type,user_id=user_id,credit_left=flag)
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