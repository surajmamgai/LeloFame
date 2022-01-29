"""Dcxa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from panel import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('',views.users),
    path('credit_purchase_request/',views.credit_purchase_request),
    path('lelofame_request/',views.lelofame_request),
    path('approve_c/',views.approve_c),
    path('reject_c/',views.reject_c),
    path('approve_l/',views.approve_l),
    path('reject_l/',views.reject_l)
]