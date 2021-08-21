import random, string

######################################################################

def randomKey():
    return "".join(random.choice(string.ascii_lowercase) for i in range(16))