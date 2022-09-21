import math
import sys
r = float(sys.argv[1])
h = float(sys.argv[2])
V = math.pi * (r*2)*h
S = 2*math.pi * r *(r+h)
print(V)
print(S)
