#array user input.

from array import*

num = array('i',[])

a = int(input("Enter array's length: "))

for i in range(a):
    b = int(input("Enter your next number: "))
    num.append(b)
print(num)

c = int(input("Search here: "))

print(num.index(c))