from django.contrib import admin
# Register your models here.
from .models import *


class ProfileLog(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]
    search_fields = ('username','name','first_name', 'last_name', 'email', 'credits')
admin.site.register(Profile,ProfileLog)
admin.site.register(CreditLog)
admin.site.register(CreditPurchaseLog)
admin.site.register(LeloFameRequest)
