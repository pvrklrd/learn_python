#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random as r
import os

os.system('cls')

random_num = r.randint(0,1)

if(random_num == 1):
    print("Heads")
elif(random_num == 0):
    print("Tails")
else:
    print("Sorry! Something went wrong technically!")