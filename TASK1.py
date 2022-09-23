import math
x=float(input('х:'))
if x <= -0.5:
    y=math.fabs((2*(x**-x))-(x**2))
elif x > -0.5 and x < 5:
    y=math.cos(x) + math.sin(2*x)
else:
    y=(x**0.5)- 9 + math.log(x)
print(y)
        