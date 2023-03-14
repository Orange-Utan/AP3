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

gitterdick = ufloat(0.5,0.05)
gitterpos = ufloat(10,0.05)-0.5*gitterdick
schirmdick = ufloat(1.6,0.05)
schirmpos = uarray([50,70,90],0.05)-0.5*schirmdick

l=[1,2,3]
for i in range(3):
    l[i]= schirmpos[i]-gitterpos
print(l)
l1 = ufloat(41.05,0.07905694150420949)
l2 = ufloat(61.05,0.07905694150420949)
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


l1_b_links = uarray(np.flip([0.0, -1.8, -3.65, -5.475, -7.35, -9.35, -11.275]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_b_rechts = uarray([1.85, 3.675, 5.55, 7.25, 9.25, 11.175],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l1_b = uarray([-11.275 , -9.35  , -7.35  , -5.475,  -3.65  , -1.8    , 0.0 ,1.85, 3.675, 5.55, 7.25, 9.25, 11.175],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)


l2_b_links = uarray(np.flip([0.0, -2.7, -5.425, -8.11, -10.86, -13.825]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_b_rechts = uarray([2.675, 5.275, 8.0, 10.7, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l2_b = uarray([-13.825, -10.86  , -8.11  , -5.425  ,-2.7 ,0.0, 2.675, 5.275, 8.0, 10.7, 13.5],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)

l3_b_links= uarray(np.flip([0.0, -3.5, -7.0, -10.8, -14.3]),(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_b_rechts = uarray([3.65, 7.25, 10.8, 14.4],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)
l3_b = uarray([-14.3 ,-10.8 , -7.0   ,-3.5  , 0.0,3.65, 7.25, 10.8, 14.4],(((0.05)/2/6**0.5)**2+((0.05)/2/6**0.5)**2)**0.5)



#n*lamda = a*sinA, s/l = tanA ---> n*lamda= sin(arctan(s/l)

fig, ax1 = plt.subplots(1,3)

def func1(s,l):
    return unumpy.sin(unumpy.arctan(s/l))

def funcfit(x,a, b):
    return a*x + b


"""def createAvg():
    avg_g = uarray([],[])
    avg_g.append(func1(l1_g[0],l1))
    avg_g.append((func1(l1_g[1],l1)+func1(l2_g[0],l2))/2)
    avg_g.append((func1(l1_g[2],l1) + func1(l2_g[1],l2)) / 2)
    for i in range(0,7):
        avg_g.append((func1(l1_g[3+i],l1) + func1(l2_g[2+i],l2) + func1(l3_g[i],l3)) / 3)
        #print(i)
    avg_g.append((func1(l1_g[3+7+1],l1) + func1(l2_g[2+7+1],l2)) / 2)
    avg_g.append(func1(l1_g[3 + 7 + 2],l1))
    return avg_g
avge_g = createAvg()
print(avge_g)"""

def plotOrange():
    ax1[0].errorbar(
        [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6],
        nominal_values(func1(l1_o,l1)),
        yerr=std_devs(func1(l1_o,l1)),
        marker='.',
        markerfacecolor = 'cyan',  # gef¨ullter Punkt
        linestyle = '',  # keine Verbindungslinie
        label=r'Messung bei Länge 1 = $(41,05 \pm 0,08)\,cm$')
    ax1[0].errorbar(
        [-5,-4,-3,-2,-1,0,1,2,3,4,5],
        nominal_values(func1(l2_o,l2)),
        yerr=std_devs(func1(l2_o,l2)),
        marker='.',
        markerfacecolor = 'blue',  # gef¨ullter Punkt
        linestyle = '',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(61,05 \pm 0,08)\,cm$')
    ax1[0].errorbar(
        [-3,-2,-1,0,1,2,3],
        nominal_values(func1(l3_o,l3)),
        yerr=std_devs(func1(l3_o,l3)),
        marker='.',
        markerfacecolor = 'purple',  # gef¨ullter Punkt
        linestyle = '',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(81,05 \pm 0,08)\,cm$')

    #mittel_o_func = (func1(l1_o,l1)+func1(l2_o,l2)+func1(l3_o,l3))/3

    popto, pcovo = curve_fit(funcfit, xdata=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6], ydata=nominal_values(func1(l1_o,l1)))
    ax1[0].plot(np.linspace(-6,6,100),funcfit(np.linspace(-6,6,100), popto[0], popto[1]), 'orange', label=r'Fit, Orange Wellenlänge')
    print(popto)
    print(np.sqrt(pcovo))
plotOrange()

def plotGreen():
    ax1[1].errorbar(
        [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
        nominal_values(func1(l1_g, l1)),
        yerr=std_devs(func1(l1_g, l1)),
        marker='.',
        markerfacecolor='cyan',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label=r'Messung bei Länge 1 = $(41,05 \pm 0,08)\,cm$')
    ax1[1].errorbar(
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        nominal_values(func1(l2_g, l2)),
        yerr=std_devs(func1(l2_g, l2)),
        marker='.',
        markerfacecolor='blue',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(61,05 \pm 0,08)\,cm$')
    ax1[1].errorbar(
        [-3, -2, -1, 0, 1, 2, 3],
        nominal_values(func1(l3_g, l3)),
        yerr=std_devs(func1(l3_g, l3)),
        marker='.',
        markerfacecolor='purple',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(81,05 \pm 0,08)\,cm$')

    # mittel_o_func = (func1(l1_o,l1)+func1(l2_o,l2)+func1(l3_o,l3))/3

    poptg, pcovg = curve_fit(funcfit, xdata=[-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
                             ydata=nominal_values(func1(l1_g,l1)))
    ax1[1].plot(np.linspace(-6, 6, 100), funcfit(np.linspace(-6, 6, 100), poptg[0], poptg[1]), 'green',
                label='Fit, Grüne Wellenlänge')
    print(poptg)
    print(np.sqrt(pcovg))
plotGreen()

def plotBlue():
    ax1[2].errorbar(
        [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
        nominal_values(func1(l1_b, l1)),
        yerr=std_devs(func1(l1_b, l1)),
        marker='.',
        markerfacecolor='cyan',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label=r'Messung bei Länge 1 = $(41,05 \pm 0,08)\,cm$')
    ax1[2].errorbar(
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        nominal_values(func1(l2_b, l2)),
        yerr=std_devs(func1(l2_b, l2)),
        marker='.',
        markerfacecolor='blue',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(61,05 \pm 0,08)\,cm$')
    ax1[2].errorbar(
        [-4, -3, -2, -1, 0, 1, 2, 3, 4],
        nominal_values(func1(l3_b, l3)),
        yerr=std_devs(func1(l3_b, l3)),
        marker='.',
        markerfacecolor='purple',  # gef¨ullter Punkt
        linestyle='',  # keine Verbindungslinie
        label='Messung bei Länge 3 = $(81,05 \pm 0,08)\,cm$')

    # mittel_o_func = (func1(l1_o,l1)+func1(l2_o,l2)+func1(l3_o,l3))/3

    poptg, pcovg = curve_fit(funcfit, xdata=[-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6],
                             ydata=nominal_values(func1(l1_b,l1)))
    ax1[2].plot(np.linspace(-6, 6, 100), funcfit(np.linspace(-6, 6, 100), poptg[0], poptg[1]), 'blue',
                label='Fit, Blaue Wellenlänge')
    print(poptg)
    print(np.sqrt(pcovg))
plotBlue()


for i in range(0,3):
    ax1[i].xaxis.set_major_locator(MultipleLocator(5))
    ax1[i].xaxis.set_minor_locator(MultipleLocator(1))
    ax1[i].grid(which='minor', color='#CCCCCC', linestyle=':')
    ax1[i].grid(which='major', color='#CCCCCC', linestyle=':')
    ax1[i].set_xlabel("Ordnung des Maximum")
    ax1[i].legend()
ax1[0].set_title('Orange Wellenlänge')
ax1[1].set_title('Grüne Wellenlänge')
ax1[2].set_title('Blaue Wellenlänge')
ax1[0].set_ylabel(r"sin(arctan($\frac{s}{l}$))")

#print(0.05841954*10*1000)


plt.show()




