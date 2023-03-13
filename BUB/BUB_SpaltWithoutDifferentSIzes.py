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
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

gitter = ufloat(20,0.05)/100+1/2*ufloat(2,0.5)/1000+ufloat(2,0.5)/1000
l1 = ufloat(70,0.05)/100+1/2*ufloat(1.6,0.05)/100-gitter
l2 = ufloat(120,0.05)/100+1/2*ufloat(1.6,0.05)/100-gitter
l3 = ufloat(190,0.05)/100+1/2*ufloat(1.6,0.05)/100-gitter

print(l1)
print(l2)
print(l3)


ordnung_1 = [-10 , -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ordnung_2 = [-11, -10 , -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ordnung_3 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l1_links = uarray(np.flip([0,0.26, 0.49, 0.66, 0.9, 1.13, 1.35, 1.56, 1.77, 1.95, 2.2]), (((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l1_rechts = uarray([0,0.29, 0.48, 0.68, 0.94, 1.15, 1.35, 1.58, 1.78, 1.97, 2.21], (((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l1_auslenkung = uarray([-1.95, -1.77, -1.56, -1.35, -1.13, -0.9, -0.66, -0.49, -0.26, 0.29, 0.48, 0.68, 0.94, 1.15, 1.35, 1.58, 1.78, 1.97], (((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100


l2_links =uarray(np.flip([0,0.44, 0.9, 1.34, 1.79, 2.21, 2.63, 3.09, 3.56, 3.92, 4.38, 4.8]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l2_rechts = uarray([0,0.47, 0.91, 1.35, 1.76, 2.27, 2.65, 3.08, 3.57, 4.0, 4.42, 4.91],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l2_auslenkung = uarray([-3.92, -3.56, -3.09, -2.63, -2.21, -1.79, -1.34, -0.9,  -0.44, 0.47, 0.91, 1.35, 1.76, 2.27, 2.65, 3.08, 3.57, 4.0],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100


l3_links = uarray(np.flip([0,0.78, 1.49, 2.21, 2.96, 3.78, 4.41, 5.17, 5.77, 6.56]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l3_rechts = uarray([0,0.78, 1.53, 2.23, 3.0, 3.74, 4.43, 5.22, 6.02, 6.61],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
l3_auslenkung = uarray([-6.56, -5.77, -5.17, -4.41, -3.78, -2.96, -2.21, -1.49, -0.78, 0.78, 1.53, 2.23, 3.0, 3.74, 4.43, 5.22, 6.02, 6.61], (((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)/100
#print(-np.flip([0,0.78, 1.49, 2.21, 2.96, 3.78, 4.41, 5.17, 5.77, 6.56]))



fig, ax = plt.subplots()

tanAlpha1 = l1_auslenkung/l1
tanAlpha2 = l2_auslenkung/l2
tanAlpha3 = l3_auslenkung/l3

tanAlphaMean = []
for i in range(0,len(tanAlpha1)):
        tanAlphaMean.append((tanAlpha1[i]+tanAlpha2[i]+tanAlpha3[i])/3)




ax.errorbar(
        ordnung_3,
        nominal_values(tanAlpha1),
        label = r'Messungen bei Länge 1 = $(50,5 \pm 0,09)\,$cm',
        color = 'purple',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        #xerr=std_devs(P_List),
        yerr=std_devs(tanAlpha1)
        )
ax.errorbar(
        ordnung_3,
        nominal_values(tanAlpha2),
        label = r'Messungen bei Länge 2 = $(100,5 \pm 0,09)\,$cm',
        color = 'red',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        #xerr=std_devs(P_List),
        yerr=std_devs(tanAlpha2)
        )
ax.errorbar(
        ordnung_3,
        nominal_values(tanAlpha3),
        label = r'Messungen bei Länge 3 = $(170,5 \pm 0,09)\,$cm',
        color = 'blue',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        #xerr=std_devs(P_List),
        yerr=std_devs(tanAlpha3)
        )

def func(x,a):
        return a*x

popt3, pcov3 = curve_fit(func, xdata=ordnung_3, ydata=nominal_values(tanAlphaMean))
ax.plot(np.linspace(-10,10,100),func(np.linspace(-10,10,100),popt3[0]),
        'green',
        label='Ausgleichsgerade, Steigung m = ' + str)


ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
ax.grid(which='major', color='#CCCCCC', linestyle=':')
ax.set_xlabel("Ordnung des Minimum")
ax.set_ylabel(r"$\frac{s}{l}$")
plt.legend()
plt.show()
