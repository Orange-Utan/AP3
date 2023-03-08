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

#Ungenau: Messkala 0,5 mm Messschieber: 0,25mm
gegenstand = 13/100
schirm = np.array([140.0, 135.0, 130.0, 125.0, 120.0, 115.0, 110.0, 105.0, 100.0, 95.0, 90.0])/100
geggroesselinks = 5/1000
bildGrLinks = np.array([30.5, 30.0, 29.0, 25.0, 22.5, 25.0, 23.0, 23.0, 20.0, 18.0, 12.0])/1000
ubildlinks = np.array([5.0, 5.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0, 3.0, 3.0])/1000
links = np.array([32.5, 32.2, 33.4, 32.7, 33.2, 33.5, 33.5, 33.05, 34.5, 34.5, 34.8])/100
ulinks = np.array([9,8.5,8,7.5,7.5,7,6.5,6,5.5,5,4.5])/1000
rechts= np.array([128.4, 122.6, 117.6, 112.5, 107.4, 102.0, 96.9, 91.8, 86.1, 79.9, 75.4])/100
urechts = np.array([6,5.5,5,4.5,4,4.5,5,5.5,6,6,6])/1000
geggroesserechts = 25/100
bildGrRechts = np.array([2.25, 2.5, 3.0, 2.5, 4.0, 4.0, 4.5, 4.5, 5.5, 7.0, 7.5])/1000
ubildrechts = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.5, 0.7])/1000

u_gegen = ufloat(gegenstand,(5/1000)/(2*np.sqrt(6)))
u_schirm= uarray(schirm, (5/1000)/(2*np.sqrt(6)))
u_geGrLinks = ufloat(geggroesselinks, (2.5/1000)/(2*np.sqrt(6))) #y
u_bildGrLinks = uarray(bildGrLinks,(ubildlinks)/(2*np.sqrt(6))) #y'
u_links = uarray(links,(ulinks)/(2*np.sqrt(6)))
u_rechts = uarray(rechts, urechts/(2*np.sqrt(6)))
u_geGrRechts = uarray(geggroesserechts,(2.5/1000)/(2*np.sqrt(6))) #y
u_bildGrRechts = uarray(bildGrRechts, ubildrechts/(2*np.sqrt(6))) #y'

#g= u_gegen - u_linse
#g'= u_schirm-u_linse

glinks1 = -abs(u_gegen - u_links)
glinks2 = abs(u_schirm - u_links)
grechts1 = -abs(u_gegen - u_rechts)
grechts2 = abs(u_schirm - u_rechts)

betalinks = u_bildGrLinks/u_geGrLinks
betarechts = u_bildGrRechts/u_geGrRechts

xg1links = 1-1/betalinks
xg2links = 1-betalinks
xg1rechts = 1-1/betarechts
xg2rechts = 1-betarechts

def func(x,f,h):
    return f*x+h


fig, ax1 =plt.subplots(1,2)
fig, ax2 = plt.subplots(1,2)



ax1[0].errorbar(
    nominal_values(xg1links),
    nominal_values(glinks1),
    std_devs(xg1links),
    std_devs(glinks1),
    marker='.',
    markerfacecolor = 'pink',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label = 'Messung bei 1V',  # Name in der Legende
)

ax1[1].errorbar(
    nominal_values(xg2links),
    nominal_values(glinks2),
    std_devs(xg2links),
    std_devs(glinks2),
    marker='.',
    markerfacecolor = 'cyan',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label = 'Messung bei 1V',  # Name in der Legende
)

popt1, pcov1 = curve_fit(func, xdata=nominal_values(xg1links), ydata=nominal_values(glinks1), p0=[0.09,-0.06] )
popt2, pcov2 = curve_fit(func, xdata=nominal_values(xg2links), ydata=nominal_values(glinks2))

ax1[0].plot(np.linspace(0,1,100),func(np.linspace(0,1,100), popt1[0],popt1[1]), 'purple', label='Fit für g bei linker konfig')
ax1[1].plot(np.linspace(-6,0,100),func(np.linspace(-6,0,100), popt2[0],popt2[1]), 'g', label='Fit für g` bei linker konfig')

ax2[0].errorbar(
    nominal_values(xg1rechts),
    nominal_values(grechts1),
    std_devs(xg1rechts),
    std_devs(grechts1),
    marker='.',
    markerfacecolor = 'pink',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label = 'Messung bei 1V',  # Name in der Legende
)

ax2[1].errorbar(
    nominal_values(xg2rechts),
    nominal_values(grechts2),
    std_devs(xg2rechts),
    std_devs(grechts2),
    marker='.',
    markerfacecolor = 'cyan',  # gef¨ullter Punkt
    linestyle = '',  # keine Verbindungslinie
    label = 'Messung bei 1V',  # Name in der Legende
)

popt3, pcov3 = curve_fit(func, xdata=nominal_values(xg1rechts), ydata=nominal_values(grechts1))
popt4, pcov4 = curve_fit(func, xdata=nominal_values(xg2rechts), ydata=nominal_values(grechts2))

ax2[0].plot(np.linspace(-150,0,100),func(np.linspace(-150,0,100), popt3[0],popt3[1]), 'purple', label='Fit für g bei linker konfig')
ax2[1].plot(np.linspace(0.95,1,100),func(np.linspace(0.95,1,100), popt4[0],popt4[1]), 'g', label='Fit für g` bei linker konfig')



print(popt1)
print(np.sqrt(pcov1))
print(popt2)
print(np.sqrt(pcov2))
print(popt3)
print(np.sqrt(pcov3))
print(popt4)
print(np.sqrt(pcov4))




plt.show()