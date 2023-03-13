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

gitterpos = ufloat(10,0.05)
gitterdick = ufloat(0.5,0.05)
schirmpos = uarray([50,70,90],0.05)
schirmdick = ufloat(1.6,0.05)

l=[1,2,3]
for i in range(3):
    l[i]= schirmpos[i]+0.5*schirmdick-(gitterpos-0.5*gitterdick)
print(l)
l1 = ufloat(41.05,0.07905694150420949)
l2=ufloat(61.05,0.07905694150420949)
l3 = ufloat(81.05,0.07905694150420949)

#Unsicherheiten zeichnen 0,05mm  messen 0,05cm

l1_o_links = uarray(np.flip([0.0, -2.36, -4.875, -7.3, -9.83, -12.525, -15.33]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_o_rechts = uarray([2.4, 4.81, 7.225, 9.73, 12.3, 15.8],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_o = uarray([-15.33 , -12.525 , -9.83  , -7.3   , -4.875  ,-2.36    ,0.0  ,2.4, 4.81, 7.225, 9.73, 12.3, 15.8],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l2_o_links = uarray(np.flip([0.0, -3.55, -7.1, -10.825, -14.55, -18.55]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_o_rechts = uarray([ 3.5, 7.05, 10.6, 14.35, 18.15],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_o = uarray([ -18.55 ,-14.55,-10.825 ,-7.1 ,-3.55  ,  0.0 ,3.5, 7.05, 10.6, 14.35, 18.15],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l3_o_links = uarray(np.flip([0.0, -4.7, -9.4, -14.15]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_o_rechts = uarray([4.7, 9.45, 14.3],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_o = uarray([-14.15 , -9.4  , -4.7   , 0.0 ,4.7, 9.45, 14.3],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l1_g_links = uarray(np.flip([0.0, -2.275, -4.525, -6.85, -9.2, -11.8, -14.5]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_g_rechts = uarray([2.25, 4.45, 6.75, 9.175, 11.575, 14.0],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_g = uarray([-14.5 ,  -11.8   , -9.2  ,  -6.85  , -4.525,  -2.275  , 0.0 ,2.25, 4.45, 6.75, 9.175, 11.575, 14.0],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l2_g_links = uarray(np.flip([0.0, -3.35, -6.21, -10.2, -13.775, -17.6]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_g_rechts = uarray([3.3, 6.6, 10.25, 13.5, 17.1],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_g = uarray([-17.6 ,  -13.775, -10.2   , -6.21  , -3.35, 0.0,3.3, 6.6, 10.25, 13.5, 17.1],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l3_g_links = uarray(np.flip([0.0, -4.45, -8.85, -13.3]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_g_rechts = uarray([4.45, 8.9, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_g = uarray([-13.3 ,-8.85 , -4.45 ,0.0, 4.45, 8.9, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)


l1_b_links= uarray(np.flip([0.0, -1.8, -3.65, -5.475, -7.35, -9.35, -11.275]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_b_links = uarray([1.85, 3.675, 5.55, 7.25, 9.25, 11.175],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_b = uarray([-11.275 , -9.35  , -7.35  , -5.475,  -3.65  , -1.8    , 0.0 ,1.85, 3.675, 5.55, 7.25, 9.25, 11.175],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)


l2_b_links = uarray(np.flip([0.0, -2.7, -5.425, -8.11, -10.86, -13.825]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_b_rechts = uarray([2.675, 5.275, 8.0, 10.7, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_b = uarray([-13.825, -10.86  , -8.11  , -5.425  ,-2.7 ,0.0, 2.675, 5.275, 8.0, 10.7, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l3_b_links= uarray(np.flip([0.0, -3.5, -7.0, -10.8, -14.3]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_b_rechts = uarray([3.65, 7.25, 10.8, 14.4],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_b = uarray([-14.3 ,-10.8 , -7.0   ,-3.5  , 0.0,3.65, 7.25, 10.8, 14.4],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

#n*lamda = a*sinA, s/l = tanA ---> n*lamda= sin(arctan(s/l)

fig, ax1 = plt.subplots()

def func1(s,l):
    return unumpy.sin(unumpy.arctan(s/l))

def funcfit(x,a,b):
    return a*x + b
#print(func1(l1_o,l1))


ax1.errorbar(
    [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6],
    nominal_values(func1(l1_o,l1)),
    yerr=std_devs(func1(l1_o,l1)),
    marker='.',
    markerfacecolor = 'cyan',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label='l1')

ax1.errorbar(
    [-5,-4,-3,-2,-1,0,1,2,3,4,5],
    nominal_values(func1(l2_o,l2)),
    yerr=std_devs(func1(l2_o,l2)),
    marker='.',
    markerfacecolor = 'cyan',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label='l2')

ax1.errorbar(
    [-3,-2,-1,0,1,2,3],
    nominal_values(func1(l3_o,l3)),
    yerr=std_devs(func1(l3_o,l3)),
    marker='.',
    markerfacecolor = 'cyan',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label='l3')

#mittel_o_func = (func1(l1_o,l1)+func1(l2_o,l2)+func1(l3_o,l3))/3

popto, pcovo = curve_fit(funcfit, xdata=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6], ydata=nominal_values(func1(l1_o,l1)))
ax1.plot(np.linspace(-6,6,100),funcfit(np.linspace(-6,6,100), popto[0],popto[1]), 'orange', label='Fit, Orange Welle')
print(popto)




fig, ax2 =plt.subplots()


plt.legend()
plt.show()


