import string
import random

# using random.choices() generating random strings
res = ''.join(random.choices(string.ascii_letters,
                             k=7)) # initializing size of string

print("The generated random string : " + str(res))
