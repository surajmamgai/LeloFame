from csv import list_dialects
from django.contrib import admin
from django.db.models.functions import Upper, Lower
# Register your models here.
from .models import *

class ProfileLog(admin.ModelAdmin):
    list_display = ['username','name','first_name', 'last_name', 'reffered_by','total_refferal','reedemed_refferal', 'email', 'credits']
    search_fields = ('username','name','first_name', 'last_name', 'email', 'credits')
    ordering = ['-date_joined']
    # def get_ordering(self, request):
    #     return [Upper('date_joined')]
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

class CredStat(admin.ModelAdmin):
    list_display = ['username', 'comment','plan','date','credit', 'amount', 'status']
    search_fields = ('username', 'comment','plan','date','credit', 'amount', 'status')
admin.site.register(CreditStatement,CredStat)

class LeloStat(admin.ModelAdmin):
    list_display = ['username', 'comment','plan','platform','date','type', 'price', 'status']
    search_fields = ('username', 'comment','plan','platform','date','type', 'price', 'status')
admin.site.register(LeloFameStatement,LeloStat)