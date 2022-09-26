import math 
#2, #3

a = int(input('a:'))
b = int(input('b:'))
h = int(input('h:'))
lst = [] #список
p = 0
x = a

while x <= b:
    y = round(math.sin(x + math.pi) + math.cos(x + math.log(abs(x))), 3)
    lst.append([x, y])
    p += y 
    x += h

p = round(p, 3)
print(p)
print(lst)