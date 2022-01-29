from django.contrib import admin
# Register your models here.
from .models import *

class ProfileLog(admin.ModelAdmin):
    list_display = ['username','name','first_name', 'last_name', 'reffered_by','total_refferal', 'email', 'credits']
    search_fields = ('username','name','first_name', 'last_name', 'email', 'credits')
admin.site.register(Profile,ProfileLog)

class LeloFame(admin.ModelAdmin):
    list_display = ['username', 'credit_spends', 'platform', 'type', 'userhandle', 'credit_left', 'date','plan'] 
    search_fields = ('username', 'credit_spends', 'platform', 'type', 'userhandle', 'credit_left', 'date','plan') 
admin.site.register(LeloFameLog, LeloFame)

class CreditPurchase(admin.ModelAdmin):
    list_display = ['username', 'credit_previous_balanace', 'credit_new_balance', 'credit_value', 'amount', 'date']
    search_fields = ( 'username', 'credit_previous_balanace', 'credit_new_balance', 'credit_value', 'amount', 'date')  
admin.site.register(CreditPurchaseLog, CreditPurchase)

class LeloFameReq(admin.ModelAdmin):
    list_display = ['username', 'userhandle', 'platform', 'type', 'plan', 'status']
    search_fields = ('username', 'userhandle', 'platform', 'type', 'plan', 'status')  
admin.site.register(LeloFameRequest)

class CreditPurchaseReq(admin.ModelAdmin):
    list_display = ['username', 'credit', 'amount', 'paymentslip', 'status']
    search_fields = ('username', 'credit', 'amount', 'paymentslip', 'status')  
admin.site.register(CreditPurchaseRequest,CreditPurchaseReq)

class Reff(admin.ModelAdmin):
    list_display = ['username', 'date', 'reffered_to']
    search_fields = ('username', 'date', 'reffered_to')  
admin.site.register(Referral, Reff)