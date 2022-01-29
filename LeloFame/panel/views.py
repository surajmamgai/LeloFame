from django.shortcuts import render,redirect
from FYIT.models import *
from FYIT import utils
from django.db.models import Sum
from django.db.models import Aggregate
# Create your views here.

def users(request):
    entry = Profile.objects.all()
    return render(request,"panel/users.html",{'u':entry})

def credit_purchase_request(request):
    entry = CreditPurchaseRequest.objects.filter(status=0)
    return render(request,"panel/credit_purchase_request.html",{'u':entry})

def lelofame_request(request):
    entry = LeloFameRequest.objects.filter(status=0)
    return render(request,"panel/lelofame_request.html",{'u':entry})

def approve_l(request):
    if request.method =='POST':
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        credit = request.POST.get('credit')
        try:
            utils.creditpurchaselog(username,amount,credit)
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=1
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

def reject_l(request):
    if request.method =='POST':
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        credit = request.POST.get('credit')
        try:
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=2
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

def approve_c(request):
    if request.method =='POST':
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        credit = request.POST.get('credit')
        try:
            utils.creditpurchaselog(username,amount,credit)
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=1
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

def reject_c(request):
    if request.method =='POST':
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        credit = request.POST.get('credit')
        try:
            obj = CreditPurchaseRequest.objects.get(username = username)
            obj.status=2
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

