from logging import exception
import re
from django.shortcuts import render, redirect
from FYIT import utils
from .models import *
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request,"index.html")

def dashboard(request):
    username = request.user
    if username.is_authenticated:
        totalspending = utils.totalspending(username)
        username=Profile.objects.get(username = username.username)
        referlink = "/signup?referral="+str(username)
        
        return render(request,"dashboard.html",{'username':username,'spending':totalspending, 'referallink':referlink})
    else:
       return redirect('login')


def creditpurchases(request):
    return redirect('creditpurchase')

#login
def signup(request):
    if request.method=="POST":
        id = (utils.generateuser())
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            reffer = request.POST.get('refferal')
            print(reffer)
            # objx = Profile.objects.get(username = reffer)
            print("Adfsdaf")
        except:
            reffer = ""
        if len(reffer)>0:
            ob2 = Referral(reffered_to = id)
            ob1 = Profile.objects.get(username = reffer)
            ob2.username = ob1
            ob2.save()
            obj =Profile.objects.create_user(username = id, first_name=first_name,reffered_by=reffer, last_name=last_name, email = email,password = password, credits = 0)
        else:
            obj =Profile.objects.create_user(username = id, first_name=first_name,last_name=last_name, email = email,password = password, credits = 0)

        password1 = request.POST.get('confirmpassword')
        if(password1!=password):
            p = "Password and Confirm Password doesn't matched!"
            return render(request,"signup.html",{'p':p})
        obj.save()
        if len(reffer)>0:
            utils.totalrefferal(reffer)
            utils.creditbenifit(reffer)
        user = authenticate(request,username=id, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
    try:
        gett = request.GET['referral']
        refferal_user = Profile.objects.get(username = gett)
        
    except:
        gett = ""
    return render(request,"signup.html",{'ref':gett})
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
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

#credit log


def mail(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        utils.send_mail_function(name,email,subject,message)
        return redirect('/')
    return redirect('/')

def lelofamerequest(request):
    user = request.user.username
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        # print(request.POST)
        userhandle = request.POST.get('userhandle')
        txn=utils.generate_txn()
        platform = request.POST.get('platform')
        type = request.POST.get('type')
        plan=request.POST.get('plan')

        username = Profile.objects.get(username = user)
        # plan = LeloFamePlan[platform][type][plan]
        obj=LeloFameRequest(txn=txn,userhandle=userhandle,platform=platform,type=type,plan=plan)
        obj.username = username
        obj.save()   
        totalspending = utils.totalspending(username)
        username=Profile.objects.get(username = username.username)
        referlink = "/signup?referral="+str(username)
        return render(request,"dashboard.html",{'username':username,'spending':totalspending,"success":1,'referallink':referlink})    
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
        print(request.POST)
        plan= request.POST.get('plan-credit')
        txn=utils.generate_txn()
        credit = Price[plan]["credit"]
        amount = Price[plan]["amount"]
        paymentslip = request.FILES.get('paymentslip')
        username=Profile.objects.get(username = username)
        obj = CreditPurchaseRequest(txn=txn,credit= credit,paymentslip=paymentslip,amount=amount)
        obj.username=username
        obj.save()
        totalspending = utils.totalspending(username)
        username=Profile.objects.get(username = username.username)
        return render(request,"dashboard.html",{'username':username,'spending':totalspending,"success":1})
    return redirect('/dashboard')
    


