from django.shortcuts import render,redirect
from FYIT.models import *
from django.db.models import Sum
from django.db.models import Aggregate
# Create your views here.

def users(request):
    entry = Profile.objects.all()
    return render(request,"panel/users.html",{'u':entry})

def credit_purchase_request(request):
    entry = CreditPurchaseRequest.objects.all()
    return render(request,"panel/credit_purchase_request.html",{'u':entry})

def lelofame_request(request):
    entry = LeloFameRequest.objects.all()
    return render(request,"panel/lelofame_request.html",{'u':entry})

def approve(request):
    if request.method =='POST':
        name = request.POST.get('user')
        try:
            username = Profile.objects.get(username=name)
            print(username)
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=1
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

def reject(request):
    if request.method =='POST':
        name = request.POST.get('user')
        print(name)
        try:
            username = Profile.objects.get(username=name)
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=2
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

