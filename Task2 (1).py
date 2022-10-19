import numpy as np
import random

arr1 = np.zeros((3, 3), dtype=int)

for i in arr1:
   
    for j in range(3):
        
        i[j] = random.randint(1, 30)

arr2 = arr1.copy()

for i in arr2:

    for j in range(3):
        
        i[j] = i[j] * 2

print(arr1)
print(arr2)

#  якщо потрібно отримати сумму відповідних елементів масивів
# for i in range(3):
#     for j in range(3):
#         arr1[i][j] = arr1[i][j] + arr2[i][j]

arr1 = np.concatenate((arr1, arr2), axis=1)

# Знаходимо сумму кутових елементів [0][0] - верхній зліва, [0][-1] - верхній праворуч, [-1][0] - нижній лівий, [-1][-1] - нижній праворуч
count = arr1[0][0] * arr1[0][-1] * arr1[-1][0] * arr1[-1][-1]

print(arr1)
print("Добуток кутових елементів дорівнює: " + str(count))
