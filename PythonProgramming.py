# print() function in python

print('Hello')
print('Welcome to India')
print()
print('I hope your are enjoying')

# end and sep in python

print('Welcome to',end=' ')
print('India')
print('20','11','2000',sep='-')

# variables in python

age = 22
name = 'Mayank'
weight = 70

print(age)
print(name)
print(weight)

price = 100
tax = 25
total_price = price + tax 
print(total_price)

# python is dynamically typed language

a = 10
print(a)
a = "Mayank"
print(a)

# more examples

is_valid = True
pi = 3.14
marks = 90
city = 'Pune'
k = None
print(is_valid,pi,marks,city,k)

# input() function in python

name = input('Enter your name: ')
age = input('Enter your age: ')
print('Welcome',name)
print('Your age is: ', age)

# python program for addition

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
add = n1+n2
print('Sum is: ',add)

# type function in python

m = 10
n = 2.43
o = 3 + 7j
print(type(m))
print(type(n))
print(type(o))

# examples of none and bool

m = True
n = None
print(type(m))
print(type(n))

# examples programs for sequence types

str = 'mayank'
print(type(str))
l = [10,20,30]
print(type(l))
t = (10,20,30)
print(type(t))
s = {10,20,30}
print(type(s))
d = {1:'am',2:'pm'}
print(type(d))

# type conversions in python includes:
# 1. implicit type conversion
# 2. explicit type conversion

# 1. implicit type conversion

a = 10
b = 1.5
c = a + b
print(c)
d = True
e = a + d
print(e)

# 2. explicit type conversion

s = '135'
i = 10 + int(s)
f = float(s)
print(i)
print(f)

s = 'Mayank'
print(list(s))
print(tuple(s))
print(set(s))

s = {10,20,30}
t = (10,20,30)
print(list(s))
print(list(t))

e = 100
print(bin(e))
print(oct(e))
print(hex(e))

a = '1000'
b = '15'
c = 'A3'
print(int(a,2))
print(int(b,8))
print(int(c,16))

# if, else and elif in python

#exampl1

n = int(input('Enter a number: '))
if n % 2 == 0:
    print("Even")
else:
    print('Odd')

# example2

a = int(input("Enter the first number: "))
b = int(input('Enter the second number: '))
if a > b :
    print('A is greater')
elif b > a :
    print('B is greater')
else:
    print('A & B are same')

# operators in python

#arithmetic operators

x = 9;
y = 4;
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

# presedence in python operators
#    ^    ** 
#    |    * / //
#    |    + -

print(5+2*3)
print(5+3*4**2)

# associativity in python operators
#    + -       left to right
#    * / //    left to right
#    **        right to left

print(5+4-2)
print(2**2**-1)
print((2**2)**-1)

# logical oeprators in python

a = 10
b = 20
c = 30
print(a < b and b < c)
print(a < b or b > c)
print(not a > b)

s1 = ''
s2 = s1 or 'DefaultStr'
print(s2)

# identity comparision operators
# is, is not

x = 10
y = x
print(x is y)
print(x is not y)

# membership comparsion operators
# in, not in

s = 'Mayank'
print('ay' in s)
print('m' in s)
print('aynak' in s)

# bitwise operators in python

# bitwise AND : &

x = 3
y = 6 
print(x & y)

# bitwise OR : |

x = 3
y = 6 
print(x | y)

# bitwise XOR : ^

x = 3
y = 6 
print(x ^ y)

# left shift operator

x = 5
print(x << 1)
print(x << 2)
print(x << 3)

# right shift operator

x = 5
print(x >> 1)
print(x >> 2)
print(x >> 3)

# bitwise NOT : ~

x = 5
print(~x)

# loops in python

# while loop

i = 0
while i < 5:
    print('Mayank')
    i += 1

i = 0
while i < 5:
    print('Mayank')
    i += 2

# range() in python

r = range(5)
print(r)
l = list(r)
print(l)

r = range(5)
print(type(r))

r = range(10,20)
l = list(r)
print(l)

r = range(10,20,2)
l = list(r)
print(l)

# for loop

l = [10,20,30,40,50]
for i in l:
    print(i)

m = 'mayank'
for i in m:
    print(i)

for x in range(5):
    print(x)

l = [10,20,30,40,50]
for i in range(len(l)):
    print(l[i])

# break in python

n = int(input('Enter a number: '))
for i in range(2,n+1):  
    if n % i == 0:
        print(i)
        break

# continue in python

l = [10,16,17,18,19,15]
for i in l:
    if i % 5 == 0:
        continue
    print(i)
    
# functions in python

def myfunc():
    print('Function called')
print('Calling Function')
myfunc()

# strings in python

print(ord('a'))
print(ord('A'))
print(chr(65))
print(chr(97))

s = 'mayank'
print(s)
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])

# strings are immutable

s = 'kathane'
s[0] = 'm'
print(s)  # error

# use of """in strings"""

s = """Good Better Best,
Love is Waste"""
print(s)

# string operations

s1 = 'hellohihello'
s2 = 'hello'
print(s2 in s1)
print(s2 not in s1)

s1 = 'hihello'
s2 = 'hi'
s3 = s1 + s2
s4 = 'good morning ' + s1 + s2
print(s3)
print(s4)

s1 = 'hellohihello'
s2 = 'hello'
print(s1.index(s2))
print(s1.rindex(s2))

s1 = 'mayank'
print(len(s1))
s2 = s1.lower()
print(s2)
s3 = s2.upper()
print(s3)
print(s1.islower())
print(s2.isupper())

s = 'hihellohi'
print(s.startswith('hi'))
print(s.endswith('hi'))

s1 = 'hi hello hi'
print(s1.split())
s2 = 'hi, hello, hi'
print(s2.split(','))
l = ['hi', 'hello', 'hi']
print(' '.join(l))
print(', '.join(l))

s = '---hihellohi---'
print(s.strip('-'))
print(s.lstrip('-'))
print(s.rstrip('-'))