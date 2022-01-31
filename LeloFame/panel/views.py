from platform import platform
from pydoc import plain
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
        txn = request.POST.get('txn')
        username = request.POST.get('username')
        credit_spends = request.POST.get('credit_spends')
        credit_left = request.POST.get('credit_left')
        platform = request.POST.get('platform')
        type = request.POST.get('type')
        plan = request.POST.get('plan')
        userhandle = request.POST.get('userhandle')
        date = request.POST.get('date')
        try:
            utils.lelofamelog(txn,username, userhandle, credit_spends,platform, type, plan)
            obj = LeloFameRequest.objects.get(txn = txn)
            obj.status=1
            obj.save()
            return redirect('/panel/lelofame_request/')
        except:
            return redirect('/panel/lelofame_request/')
    return redirect('/panel/lelofame_request/')

def reject_l(request):
    if request.method =='POST':
        txn = request.POST.get('txn')
        try:
            obj = LeloFameRequest.objects.get(txn = txn)
            obj.status=2
            obj.save()
            return redirect('/panel/lelofame_request/')
        except:
            return redirect('/panel/lelofame_request/')
    return redirect('/panel/lelofame_request/')

def approve_c(request):
    if request.method =='POST':
        txn = request.POST.get('txn')
        username = request.POST.get('username')
        amount = request.POST.get('amount')
        credit = request.POST.get('credit')
        date = request.POST.get('date')
        print(request.POST)
        try:
            utils.creditpurchaselog(txn,username,amount,credit,date)
            obj = CreditPurchaseRequest.objects.get(txn=txn)
            obj.status=1
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except Exception as e:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

def reject_c(request):
    if request.method =='POST':
        txn = request.POST.get('txn')
        try:
            obj = CreditPurchaseRequest.objects.get(txn=txn)
            obj.status=2
            obj.save()
            return redirect('/panel/credit_purchase_request/')
        except:
            return redirect('/panel/credit_purchase_request/')
    return redirect('/panel/credit_purchase_request/')

