from django.contrib import admin
from django.urls import path,include
from FYIT import views

urlpatterns = [ 
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('login', views.loginn,name='login'),
    path('signup',views.signup),
    path('contact_us',views.mail),
    path('lelofamerequest', views.lelofamerequest),
    path('logout',views.logoutt),
    path('creditpurchases',views.creditpurchases),
    # path('planrequest', views.planrequest),
    path('creditpurchase', views.creditpurchase, name ='creditpurchase'),
]