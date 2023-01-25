import os
def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

std_scrs = input("Input a list of student heights : ").split(",")

h_scr = 0

for scr in std_scrs:
    if(h_scr < int(scr)):
        h_scr = int(scr)

print(f"\n\tThe highest score in the class is : {h_scr}\n")