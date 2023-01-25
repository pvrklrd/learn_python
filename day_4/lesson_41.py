# import random package and has a rich set of functions
import random as r #import random
import os

os.system("cls")
print(r.randint(1,100)) # print any integer between 1 and 100

random_number = r.randint(5,10)
print(random_number)

random_float = r.random() # This will always return a decimal number between 0 and 1
print(random_float)


rand_flt = r.random()*5.0 # Just to get random decimal number between 0 and 5
print(rand_flt)
print(round(rand_flt,2))
