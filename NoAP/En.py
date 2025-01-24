import numpy as np

Z = 1
e = 1.602*10**-19
e0 = 8.8541878128*10**-12
hbar =  1.054571817*10**-34  #Joule
mu = 9.1093837 * 10**-31 #kg

ab = 5.29177210903*10**-11
#ab = 4*np.pi*e0*hbar**2/(mu * e**2)

def rn(n):
    return n**2*ab/Z

def En(n):
    Rn = rn(n)
    return - Z**2*e**2/(2*4*np.pi*e0*Rn)
def Eunendlich():
    return e**2/(8*np.pi*e0*ab)

print(Eunendlich()/e)

print(hbar*2*np.pi*3*10**8/(En(3)-En(2)))