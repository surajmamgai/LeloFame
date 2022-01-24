from django.shortcuts import render, redirect
from django.http import HttpResponse

from FYIT.models import *
from django.contrib.auth import authenticate, login, logout

def dashboard(request):
    return render(request,'paneldashboard.html')
