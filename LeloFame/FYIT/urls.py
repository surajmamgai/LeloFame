from django.contrib import admin
from django.urls import path,include
from FYIT import views

urlpatterns = [ 
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('login', views.loginn),
    path('signup',views.signup),
    path('temp',views.creditpurchase),
    path('contact_us',views.mail),
    path('lelofarmrequest', views.lelofamerequest),
    # path('planrequest', views.planrequest),
    path('creditpurchase', views.creditpurchase),
]