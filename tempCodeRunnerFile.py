# static methods

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod
    def isAdult(age):
        return (age > 18)
    def printDetails(self):
        print(self.name)
        print(self.age)
        print(Person.isAdult(self.age))
p = Person('Mayank',22)
p.printDetails()
print(Person.isAdult(24))