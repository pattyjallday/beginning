import string
import re
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(12, 24)))
password = re.sub('[`~\|/_]', '4', password)
print (password)