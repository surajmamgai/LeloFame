import random
from .models import Profile
def generateuser():
    r = random.randint(10000001,99999998)
    u = Profile.objects.filter(id = r).count()
    if u > 0:
        generateuser()
    else:
        return r
    u = generateuser()

def left_credit(user,to_deduct):
    obj = Profile.objects.get(id=user)
    total = obj.credit
    if(total>=to_deduct):
        return total-to_deduct
    else:
        return -1