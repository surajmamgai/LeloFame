from django.contrib import admin
from django.urls import path,include
from AdminPanel import views

urlpatterns = [ 
    path('',views.dashboard),
   
]