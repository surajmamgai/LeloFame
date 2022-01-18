from django.contrib import admin
from django.urls import path,include
from FYIT import views

urlpatterns = [ 
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('login', views.login),
    path('signup',views.signup)
]