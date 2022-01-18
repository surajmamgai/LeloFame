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
