from django.contrib import admin
from django.urls import path,include
from FYIT import views

urlpatterns = [ 
    path('',views.index),
]