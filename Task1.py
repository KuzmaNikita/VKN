from array import * 
from math import pow
import random

n = int(input("Введіть число n: ")) 

arr = array('f', []) 

for i in range(n): 
    arr.append(float(pow(0.5, i)))
     
for i in range(n):
    x = arr.append(random.randint(-1, 3)) 

arr = array("f", sorted(arr.tolist(), reverse=True))
print(arr)


arr.remove(arr[-1])
arr.remove(arr[-1])


arr.remove(arr[0])
arr.remove(arr[0])

print(arr)
