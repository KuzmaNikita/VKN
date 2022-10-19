from math import sqrt

#1. Три кортежі містять координати X, Y, Z точок у просторі. Програма 
# повинна: 1) записати у список відстані від цих точок до центра координат; 2) 
# вивести індекс точки, найближчої до початку координат; 3) вивести координати 
# точки, найдільшої від центру координат. 

tuples = [(-5, 8, 4), (-1, 2, -3), (3.4, 52, 9)]
max_distant_dot = (0, ())
list_of_distants = []

for i in tuples:
    x, y, z = i
    distant = round(sqrt(x ** 2 + y ** 2 + z ** 2), 4)
    list_of_distants.append(distant)

    if distant > max_distant_dot[0]:
        max_distant_dot = (distant, i)

print(f"Відстані від точок до центру координат - {list_of_distants}")
print(f"Індекс найближчої до центру точки - {list_of_distants.index(min(list_of_distants))}")
print(f"Координати найдальшої від центру точки - {max_distant_dot[1]}")