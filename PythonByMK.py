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