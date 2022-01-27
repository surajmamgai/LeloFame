from django.shortcuts import render, redirect
from django.http import HttpResponse
from FYIT import utils
from .models import *
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request,"index.html")

def dashboard(request):
    user = request.user.username
    print(user)
    if user is None: 
        return redirect('login')
    # username = Profile.objects.get(username = user)
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
        obj.save()
        return redirect('login')
    return render(request,"signup.html",{'p':''})
#login
def loginn(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    if request.method=="POST":
        username = request.POST.get('id')
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(request,username=username, password=password)
        obj = Profile.objects.filter(username=username,password=password).count()
        # print(obj)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
        else:
            p = "Please Enter the valid Credentials"
            return render(request,"login.html",{'p':p})
    return render(request,'login.html',{'p':''})

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

Price = {
    'basic': {
        'credit': 50,
        'amount': 299
    },
    'prime': {
        'credit': 120,
        'amount': 499
    },
    'premium': {
        'credit': 200,
        'amount': 999
    }
}
def lelofamerequest(request):
    user = request.user.username
    if user is None:
        return redirect('login')
    if request.method == 'POST':
        userhandle = request.POST.get('userhandle')
        platform = request.POST.get('platform')
        type = request.POST.get('type')
        plan=request.POST.get('plan')
        username = Profile.objects.get(username = user)
        # plan = LeloFamePlan[platform][type][plan]
        obj=LeloFameRequest(username=username,userusername=userhandle,platform=platform,type=type,plan=plan)
        obj.save()       
        return redirect('dashboard/')
    return redirect('dashboard/')

Price = {
    'basic': {
        'credit': 50,
        'amount': 299
    },
    'prime': {
        'credit': 120,
        'amount': 499
    },
    'premium': {
        'credit': 200,
        'amount': 999
    }
}

def creditpurchase(request):   
    username = request.user.username
    if username is None:
        return redirect('login')

    if request.method == 'POST':
        plan= request.POST.get('plan')
        credit = Price[plan]["credit"]
        amount = Price[plan]["amount"]
        paymentslip = request.FILES.get('paymentslip')
        username=Profile.objects.get(username = username)
        obj = CreditPurchaseRequest(credit= credit,paymentslip=paymentslip, amount=amount)
        obj.username=username
        obj.save()
        return redirect('dashboard/')
    return render(request,'creditpurchase.html')





        






    return render(request,'creditpurchase.html')
        




