# Classes and Objects in Python

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def print(self):
        print(str(self.real) + " + i" + str(self.imag))
        
    def add(self, c):
        self.real += c.real
        self.imag += c.imag

c1 = Complex(10,20)
c1.print()
c2 = Complex(20,30)
c2.print()
c1.add(c2)
c1.print()

# class and instance variables

class Employee:
    compName = 'ABC'
    def __init__(self,id):
        self.id = id
e = Employee(101)
print(e.compName)
print(e.id)
print(Employee.compName)


class Employee:
    compName = 'ABC'
    def __init__(self,id):
        self.id = id
e1 = Employee(1011)
e2 = Employee(1012)
Employee.compName = 'ABCDEFGHI'
print(e1.compName)
print(e2.compName)


class Employee:
    compName = 'ABC'
    def __init__(self,id):
        self.id = id
    def fun(self,name):
        self.name = name
e = Employee(103)
e.fun('Mayank')
print(e.name)
e.designation = 'DS'
print(e.designation)


# class member access in python

# 1. In python every member is accessible everywhere

class Test:
    def __init__(self,x,y):
        self.x = x
        self.y = y
t = Test(11,33)
print(t.x)
print(t.y)

# 2. When we use underscore before variable name, we suggest not to use it outside the class

class Test:
    def __init__(self,x,y):
        self._x = x
        self.y = y
    def _fun(self):
        print('Hi')
t1 = Test(10,20)
print(t1._x)
print(t1.y)

# 3. When we use two underscores it becomes inaccessible

class Test:
    def __init__(self,x,y):
        self.__x = x
        self.y = y
    def __fun(self):
        print('Hi')
t2 = Test(1,2)
print(t2.__x)
print(t2.y)