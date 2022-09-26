import math 

# 1, #3
a = float(input('a:'))
b = float(input('b:'))
h = float(input('h:'))
lst = [] #список
p = 0
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