import numpy as np
from uncertainties.unumpy import uarray
from uncertainties import ufloat

def u (m):
    u1 = 5/100/3**0.5*m
    u2 = 8*0.01/3**0.5
    u3 = 0.01/3**0.5
    u4 = 0.02
    return (u1**2+u2**2+u3**2+u4**2)**0.5


SpannungBeschlMaxQ = np.array([3.18, 3.81, 4.17])
u_SpannungBeschlMaxQ = uarray(SpannungBeschlMaxQ,u(SpannungBeschlMaxQ))
SpannungBeschlMinQ = np.array([3.34, 3.94, 4.38])
u_SpannungBeschlMinQ = uarray(SpannungBeschlMinQ,u(SpannungBeschlMinQ))

delta = []
delta.append(u_SpannungBeschlMaxQ[1]-u_SpannungBeschlMaxQ[0])
delta.append(u_SpannungBeschlMaxQ[2]-u_SpannungBeschlMaxQ[1])
delta.append(u_SpannungBeschlMinQ[1]-u_SpannungBeschlMinQ[0])
delta.append(u_SpannungBeschlMinQ[2]-u_SpannungBeschlMinQ[1])

m = (delta[0]+delta[1]+delta[2]+delta[3])/4

print(m)

#####################################################


SpannungBeschlMaxN = np.array([1.99, 3.85, 5.73, 7.81])
u_SpannungBeschlMaxN = uarray(SpannungBeschlMaxN,u(SpannungBeschlMaxN))
SpannungBeschlMinN = np.array([2.7, 4.82, 6.89])
u_SpannungBeschlMinN = uarray(SpannungBeschlMinN,u(SpannungBeschlMinN))

delta = []
delta.append(u_SpannungBeschlMaxN[1]-u_SpannungBeschlMaxN[0])
delta.append(u_SpannungBeschlMaxN[2]-u_SpannungBeschlMaxN[1])
delta.append(u_SpannungBeschlMaxN[3]-u_SpannungBeschlMaxN[2])
delta.append(u_SpannungBeschlMinN[1]-u_SpannungBeschlMinN[0])
delta.append(u_SpannungBeschlMinN[2]-u_SpannungBeschlMinN[1])

m1 = (delta[0]+delta[1]+delta[2]+delta[3]+delta[4])/5

print(m)

h= 4.136e-15
c = 2.9979e8


lam = h*c/m
print(lam)

lam1 = h*c/m1
print(lam1)