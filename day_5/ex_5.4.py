import os
def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

for number in range(1,101):
    if(number%3==0 and number%5==0):
        print(f"\t 💚💜  FizzBuzz")
    elif(number%3==0 and number%5!=0):
        print(f"\t 💚  Fizz")
    elif(number%3!=0 and number%5==0):
        print(f"\t 💜  Buzz")
    else:
        print(f"\t {number}")
