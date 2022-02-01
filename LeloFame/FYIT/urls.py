from django.contrib import admin
from django.urls import path,include
from FYIT import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('login', views.loginn,name='login'),
    path('signup',views.signup, name = 'signup'),
    path('contact_us',views.mail, name='contact_us'),
    path('lelofamerequest', views.lelofamerequest, name = 'lelofamerequest'),
    path('logout',views.logoutt, name='logout'),
    path('creditpurchases',views.creditpurchases, name= 'creditpurchases'),
    # path('planrequest', views.planrequest),
    path('creditpurchase', views.creditpurchase, name ='creditpurchase'),
    
]