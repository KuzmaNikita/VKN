import math 
# 1, #3

a = float(input('a:'))
b = float(input('b:'))
h = float(input('h:'))
lst = [] #список
p = 0 #сумма
x = a

for i in range(1000):
    y = round(math.sin(x + math.pi) + math.cos(x + math.log(abs(x))), 3)
    #метод для добавления элемента в конец списка
    lst.append([x, y])
    p += y #добавляем к текущей сумме значение у
    x += h
    if x > b:
        break
p = round(p, 3)
print(p)
print(lst)

# 2
i = a
p = 0
lst = []

while i <= b:
    y = round(math.sin(i + math.pi) + math.cos(i + math.log(abs(i))), 3)
    lst.append([i, y])
    p += y 
    i += h

p = round(p, 3)
print(p)
print(lst)


