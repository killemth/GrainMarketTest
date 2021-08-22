"""
Key Randomizer Methods.
"""

import random
import string

######################################################################

def randomKey():
    """
    Generates a Locally Random String.  Not Unique & Distributed Safe.
    """
    return "".join(random.choice(string.ascii_lowercase) for i in range(16))
