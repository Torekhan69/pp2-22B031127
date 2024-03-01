"""Write a Python program with builtin function to multiply all the numbers in a list"""

l1 = [1,2,3,4,5,6,7]
l2 = map(lambda x:x*3,l1)
print(list(l2))

"""Write a Python program with builtin function that accepts a string and 
calculate the number of upper case letters and lower case letters"""

def num(s):
    u,l=0,0
    for i in s:
        if i.isupper(): u+=1
        elif i.islower(): l+=1
    print(u,l)
num("Hello Barn")

#or

s = "Hello Barn"
print(len(list(filter(lambda s:s.isupper(),s))))
print(len(list(filter(lambda s:s.islower(),s))))


"""Write a Python program with builtin function that checks whether a passed string is palindrome or not."""

pal_is = "lannal"

if ''.join(reversed(pal_is))==pal_is:
    print("Yes")
else: print("No")

"""Write a Python program that invoke square root function after specific milliseconds."""

import time
s = int(input("Enter a number: "))
time.sleep(2.123)
print(s**0.5)

"""Write a Python program with builtin function that returns True if all elements of the tuple are true."""

tup1 = (1,2,3,4,5,6,7)
tup1_not = (1,2,3,4,5,6,7,0)
print(all(tup1))
print(all(tup1_not))