from random import uniform

# 2. Множина С містить випадкові дійсні числа (в діапазоні від 0,7 до 150). 
# Множину D утворено з дійсних чисел, заданих користувачем. Програма 
# повинна визначити суму і різницю множин. 

d = set()
c = set()

while True:
    number = input("Введіть дійсне число, ввод буде закінчено коли введено порожню строку - ")
    
    if number == "":
        break
    else:
        d.add(float(number))
        c.add(round(uniform(0.7, 150), 4))  
    
print(d|c)
print(d - c)
