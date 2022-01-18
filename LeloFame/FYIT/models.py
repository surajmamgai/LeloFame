from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from numpy import ma
from django.utils import timezone

class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)
    credits =  models.IntegerField(default=0)

    def Id(self, *args, **kwargs):
        a = self.id
        obj = Profile.objects.get(id=a)
        n = obj.Id
        return n
    
    def Name(self, *args, **kwargs):
        a = self.id
        obj = Profile.objects.get(id=a)
        n = obj.name
        return n
    
    def Credit(self, *args, **kwargs):
        a = self.id
        obj = Profile.objects.get(id=a)
        n = obj.credit
        return n
    
    def Email(self, *args, **kwargs):
        a = self.id
        obj = Profile.objects.get(id=a)
        n = obj.email_id
        return n
    

class CreditLog(models.Model):
    idd = models.ForeignKey(Profile, on_delete=models.CASCADE)
    credit_spends = models.IntegerField()
    platform = models.CharField(max_length=200)                  # facebook, instagram, youtube etc.
    type = models.CharField(max_length=200)                      #like or share or subscribe or followers etc.
    userid = models.CharField(max_length=200)                    # user id of the platform
    credit_left = models.IntegerField()
    date = models.DateTimeField(default = timezone.now())


class CreditPurchaseLog(models.Model):
    idd = models.ForeignKey(Profile, on_delete=models.CASCADE)
    credit_previous_balanace = models.IntegerField()
    credit_new_balance = models.IntegerField()
    credit_value = models.IntegerField()                         # how much is purchased
    amount = models.IntegerField()                               #price of credits
    date = models.DateTimeField(default=timezone.now())          #date of purchase


class LeloFameRequest(models.Model):
    idd = models.ForeignKey(Profile, on_delete=models.CASCADE)
    userid = models.CharField(max_length=200)                   # platform user id like instagram id facebookid etc
    platform = models.CharField(max_length=200)                 # platform like instagram 
    type = models.CharField(max_length=200)                     # like followers etc
    request = models.CharField(max_length=300)                  # package the user selected
