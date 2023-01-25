# Instructions
# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

row1=['∎', '∎', '∎']
row2=['∎', '∎', '∎']
row3=['∎', '∎', '∎']

map = [row1,row2,row3]
#print(map)
print(f"\nThe initial matrix is :- \n{row1} \n{row2} \n{row3}\n")

c=int(input("Enter the column: "))
r=int(input("Input the row: "))
map[c-1][r-1]= '💝'

print(f"\nThe matrix after update :- \n\t{row1} \n\t{row2} \n\t{row3}\n")