
class Test:
    def __init__(self,x,y):
        self.__x = x
        self.y = y
    def __fun(self):
        print('Hi')
t2 = Test(1,2)
print(t2.__x)
print(t2.y)