import matplotlib.pyplot
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import scipy
from scipy import optimize
from scipy.optimize import curve_fit
from uncertainties import unumpy
from uncertainties.unumpy import uarray, std_devs, nominal_values
from uncertainties import ufloat
from uncertainties import unumpy as unp
import uncertainties.umath as umath
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import  generalFunctions as gf


def func(n,m):
    if m**2+n**2-n*m*(n+m) == 2023:
        return True
    else:
        return False
'''

lsg = []

r=100000
for i in range(-r,r):
    for j in range(-r,i):
        if func(i,j) == True:
            lsg.append([i,j])
        #print([i,j])
    print(lsg)
    print(i)


print(lsg)

'''

def f(n,m):
    return m**2+n**2-n*m*(n+m)-2023

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

'''print(axes3d.get_test_data(0.05))
X, Y = np.meshgrid(np.linspace(-3000, 3000, 5000), np.linspace(-3000, 3000, 5000))
Z = f(X,Y)
print(f(1,-2022))
ax.contour(X, Y, Z, extend3d=True,  cmap=cm.coolwarm)  # Plot contour curves'''
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')


r = 20
for i in range(-r,r):
    sequence_containing_x_vals = np.array(np.linspace(-2000000,2000000,50))
    sequence_containing_y_vals = np.array(np.linspace(100000*i,100000*i,50))
    sequence_containing_z_vals = f(sequence_containing_x_vals,sequence_containing_y_vals)

    index = 0
    for a in sequence_containing_x_vals:
        if(f(a,100000*i)<100 and f(a,100000*i)>-100):
            sequence_containing_x_vals[index] = -15
            sequence_containing_y_vals[index] = -15
    print(sequence_containing_x_vals)
    print(sequence_containing_z_vals)
    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
plt.show()
ax.set_aspect('auto')
ax.set_zlim([0, 5.00])
ax.set_zbound(lower=0.0, upper=5.00)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()