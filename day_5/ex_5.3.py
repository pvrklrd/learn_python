import os
def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

sum = 0
for i in range(2,101,2):
    sum += i
print(f"\n\tSum of all even number between '1' and '100' is : {sum}\n")