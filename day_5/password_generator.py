import random as r
import os
def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n\tWelcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# pwd = ""
# for i in range(1,nr_letters+1):
#     pwd += letters[r.randint(0,51)]
# for i in range(1,nr_symbols+1):
#     pwd += symbols[r.randint(0,8)]
# for i in range(1,nr_numbers+1):
#     pwd += numbers[r.randint(0,9)]
# print(pwd)

passwd = ""
pc = nr_letters + nr_numbers + nr_symbols +1
cl = 0
cn = 0
cs = 0
lst = [letters,numbers,symbols]

for cnt in range(1,pc):
    ch = r.randint(1,3)
    if(ch==1 and cl<nr_letters):
        cl += 1
        for i in range(0,nr_letters-1):
            passwd += lst[0][r.randint(0,51)]
    elif(ch==2 and cn<nr_numbers):
        cn += 1
        for i in range(0,nr_numbers-1):
            passwd += lst[1][r.randint(0,9)]
    elif(ch==2 and cs<nr_symbols):
        cs += 1
        for i in range(0,nr_symbols-1):
            passwd += lst[2][r.randint(0,8)]

print(passwd)

