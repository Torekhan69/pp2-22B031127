"""Create a generator that generates the squares of numbers up to some number N."""
'''
def gen(N):
    for i in range(N+1):
        yield i**2

for i in gen(N:=int(input())):
    print(i) 
'''
"""Write a program using generator to print the even numbers between 0 and n in 
comma separated form where n is input from console."""
'''
def gen1(N):
    for i in range(N+1):
        if i%2==0:
            yield i
list1=[]
for i in gen(N:=int(input())):
    list1.append(str(i))
print(','.join(list1))
'''
"""Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n."""
'''
def gen2(N):
    for i in range(N+1):
        if i%4==0 and i%3==0:
            yield i
for i in gen2(N:=int(input())):
    print(i)
'''
"""Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values."""
'''
def square(a,b):
    for i in range(a,b+1):
        yield i**2
for i in square(3,7):
    print(i)
'''
"""Implement a generator that returns all numbers from (n) down to 0."""
'''
def gen3(n):
    for i in range(n,-1,-1):
        yield i
for i in gen3(7):
    print(i)
'''







