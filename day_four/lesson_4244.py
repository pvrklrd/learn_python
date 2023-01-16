import random as r

numbers = [1,2,3,4,5,6,7,8,9,0]
print(numbers)

# for i in numbers:
#     print(i)

numbers.append(10)
print(numbers)

numbers.insert(0,-1)
print(numbers)

numbers.reverse()
print(numbers)

print(numbers[-1])

my_names = input(f"Give me the names : ")
names = my_names.split(", ")
print(names)
print(len(names))
print(f"The random name generated is : {names[r.randint(0,len(names)-1)]}")