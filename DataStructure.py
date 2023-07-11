# 1. Lists

l = [10,20,30,40,50]
print(l)
print(l[1])
print(l[2])
print(l[-1])

l = [10,20,30,40,50]
l.append(15)
print(l)
print(l.count(30))
print(l.index(50))

l = [10,20,30,40,50,60,70,80]
l.remove(20)
print(l)
l.pop()
print(l)
l.pop(2)
print(l)
del l[1]
print(l)
del l[0:2]
print(l)


# 2. Tuple

t = (10,20,'messi')
print(t)
t = ()
print(type(t))
print(t)
t = (10)
print(type(t))
t = (10,)
print(type(t))

t = 10,20,30,40,50,30
print(t[3])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.count(30))
print(t.index(30))