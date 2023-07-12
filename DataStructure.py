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

# 3. Set

s = {10,20,30}
print(s)
s1 = set([20,30,40])
print(s1)
s2 = { }
print(type(s2))
s3 = set()
print(type(s3))
print(s3)

s = {10,20}
s.add(30)
print(s)
s.add(30)
print(s)
s.update([30,40])
print(s)
s.update([50,60],[70,80])
print(s)

s = {10,20,30,40}
s.discard(30)
print(s)
s.remove(10)
print(s)
s.clear()
print(s)

s1 = {2,4,6,8}
s2 = {3,6,9}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

# 4. Dictionary

d = {101 : 'abc', 102 : 'pqr', 103 : 'xyz'}
print(d)
d = { }
d['laptop'] = 72000
d['mobile'] = 45000
d['earphone'] = 2500
print(d)
print(d['mobile'])