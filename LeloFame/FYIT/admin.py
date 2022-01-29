from django.contrib import admin
# Register your models here.
from .models import *

class ProfileLog(admin.ModelAdmin):
    list_display = ['username','name','first_name', 'last_name', 'reffered_by', 'email', 'credits']
    search_fields = ('username','name','first_name', 'last_name', 'email', 'credits')
admin.site.register(Profile,ProfileLog)
admin.site.register(LeloFameLog)
admin.site.register(CreditPurchaseLog)
admin.site.register(LeloFameRequest)
admin.site.register(CreditPurchaseRequest)
admin.site.register(Referral)