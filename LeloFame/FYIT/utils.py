import random
from django.core.mail import send_mail
from .models import *


def generateuser():
    r = random.randint(10000001,99999998)
    u = Profile.objects.filter(username = r).count()
    if u > 0:
        generateuser()
    else:
        return str(r)
    u = generateuser()



def left_credit(user,to_deduct):
    obj = Profile.objects.get(id=user)
    total = obj.credit
    if(total>=to_deduct):
        return total-to_deduct
    else:
        return -1


#Sending mails
def send_mail_function(name,email,subject,message):
    mess = f'Thanks for contacting us {name}. Our team will contact you soon.'
    mess +='\n'
    mess += f'Your message was:'
    mess+= f'Subject-{subject}' 
    mess+='\n'
    mess+=f'Message -{message}'
    send_mail('LELOFAME',mess,'lelo.fame.12@gmail.com',[email],fail_silently=False,)


def creditpurchaselog(username,amount,credit):
    obj = Profile.objects.get(username=username)
    obj2 = CreditPurchaseLog(credit_previous_balanace=obj.Credit(),credit_new_balance = obj.Credit()+credit,credit_value=credit,amount = amount)
    obj.credits = obj.Credit()+credit
    obj2.username = username
    obj.save()
    obj2.save()

def lelofamerequestpossible(username, credit):
    obj = Profile.objects.get(username = username)
    if obj.Credit()<credit:
        return False
    else:
        return True



def lelofamelog(username, userhandle, credit,platform, type, plan):
    obj = Profile.objects.get(username = username)
    if lelofamerequestpossible(username,credit)==False:
        return False
    obj2 = LeloFameLog(credit_spends=credit,platform=platform,type=type,userhandle=userhandle,plan=plan,credit_left=obj.Credit()-credit)
    obj.credits = obj.Credit()-credit
    obj2.username = username
    obj2.save()
    return True



def totalspending(username):
    obj = LeloFameLog.objects.filter(username = username)
    print(obj)
    x = 0
    for o in obj:
        x = x+ o.credit_spends
    return x



