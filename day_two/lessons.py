print("Hello Wolrd"[6])
print("123" + "345")
print(123 + 456)
print(int("123")+int("456"))
print(True)

print("Your name has "+str(len(input("Enter your name :")))+ " characters")

#PEMDAS or BODMAS
print(3*3+3/3-3) # is equal to (3*3) + (3/3) - 3 => 7.0

# roundoff, decimal points and floor division
print(8/3)
print(int(8/3))
print(round(8/3))
print(round(8/3,2))
print(8//3)

result = 100/5
result /= 5
number = 100/2
number //= 5
print(result)
print(number)

print(f"The divided number by 2 and 5 is {number}") # f-string

print(f"The divided number by 5 is {result:.3f}") # ':.nf' no of decimal places you need irrespective of actual calculated
# or formatted_result = "{:.2f}".format(result)
formatted_result = "{:.2f}".format(result)
print(formatted_result)