import math
t=float(input('t:'))
n=float(input('n:'))
k=float(input('k:'))
def addiction(t,n,k):
    S=float(4.17*math.sqrt(t))-math.sin(math.pi*(n)+math.pi/7)+pow(math.e,(k/t+n))
    return(S)
print(addiction(t,n,k))
