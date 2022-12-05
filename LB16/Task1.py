import matplotlib.pyplot as plt
import math
import numpy as np 


# 1. Зобразити графік функції 𝑦 = sin(0,4𝑥) + 0,1𝑥, 𝑥 ∈ [−10; 10], тип лінії – 
# суцільна, колір лінії – червоний. Зберегти графік у файл x.png.
 



x = np.linspace(-10, 10, 50, endpoint=True)


def my_func(x):
    return math.sin(0.4 * x) + 0.1 * x

y = [my_func(i) for i in x]



plt.plot(x, y, "r-", label="y = sin(0,4x) + 0,1x")

 
plt.xlabel('x') 
plt.ylabel('y')  
plt.legend()  
plt.savefig('x.png')


plt.show()