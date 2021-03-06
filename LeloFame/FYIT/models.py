from lib2to3.pytree import Base
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from numpy import ma
from django.utils import timezone



class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)
    credits =  models.IntegerField(default=0)
    reffered_by = models.CharField(max_length=300,null=True,default="999999")
    total_refferal = models.IntegerField(default=0)
    reedemed_refferal = models.IntegerField(default=0)

    def Username(self, *args, **kwargs):
        a = self.username
        obj = Profile.objects.get(username=a)
        n = obj.username
        return n
    
    def Name(self,*args,**kwarg):
        a = self.username
        obj = Profile.objects.get(username=a)
        name = obj.first_name+" "+obj.last_name
        return name
        
    def Credit(self, *args, **kwargs):
        a = self.username
        obj = Profile.objects.get(username=a)
        n = obj.credit
        return n
    
    def Email(self, *args, **kwargs):
        a = self.username
        obj = Profile.objects.get(username=a)
        n = obj.email_username
        return n

    def __str__(self):
        return self.username
    

class LeloFameLog(models.Model):
    txn = models.CharField(max_length=10,primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    credit_spends = models.IntegerField()
    platform = models.CharField(max_length=200)                  # facebook, instagram, youtube etc.
    type = models.CharField(max_length=200)                      #like or share or subscribe or followers etc.
    userhandle = models.CharField(max_length=200)                # user username of the platform
    credit_left = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)
    plan = models.CharField(max_length=300)

class CreditPurchaseLog(models.Model):
    txn = models.CharField(max_length=10,primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    credit_previous_balanace = models.IntegerField()
    credit_new_balance = models.IntegerField()
    credit_value = models.IntegerField()                         # how much is purchased
    amount = models.IntegerField()                               #price of credits
    date = models.DateTimeField(default=timezone.now)          #date of purchase

class CreditPurchaseRequest(models.Model):
    txn = models.CharField(max_length=10,primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    paymentslip = models.FileField(upload_to='paymentslip/',null=True)
    status = models.IntegerField(default=0)

class LeloFameRequest(models.Model):
    txn = models.CharField(max_length=10,primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    userhandle = models.CharField(max_length=200)              # platform user username like instagram username facebook username etc
    platform = models.CharField(max_length=200)                 # platform like instagram 
    type = models.CharField(max_length=200)                     # like followers etc
    plan = models.CharField(max_length=300)                  # package the user selected
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)



class Referral(models.Model):
    username = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    reffered_to = models.CharField(max_length=200)
    now = models.CharField(max_length=50, null=True)



class CreditStatement(models.Model):
    username = models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    plan = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=50)

class LeloFameStatement(models.Model):
    username = models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    plan = models.CharField(max_length=50)
    platform = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50)
