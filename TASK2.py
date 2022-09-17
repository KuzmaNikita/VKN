import math;
r = float(input("Радіус "));
h = float(input("Висота "));
V = math.pi * (r*2)*h;
S = 2*math.pi * r *(r+h);
print(V);
print(S);
