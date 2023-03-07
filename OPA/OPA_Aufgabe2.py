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


'''gegenstand_b = [17.0, 18.0, 20.0, 19.0, 19.0]
kabs_b = [27.0, 28.05, 30.1, 29.0, 28.9]
labs_b = [27.1, 28.2, 29.9, 29.2, 29.0]
spiegel_b = [40.0, 32.0, 34.0, 34.0, 34.0]'''


gegenstand_b = np.array([19.0, 19.0, 19.0, 19.0, 19.0])/100
kabs_b = np.array([29.0, 29.05, 29.1, 29.0, 28.9])/100
labs_b = np.array([29.1, 29.2, 28.9, 29.2, 29.0])/100
#spiegel_b = [42.0, 33.0, 33.0, 34.0, 34.0]

'''gegenstand_g = [17.0, 16.1, 19.0, 15.5, 18.0]
kabs_g = [24.5, 23.45, 26.4, 22.9, 25.45]
labs_g = [24.6, 23.65, 26.55, 23.0, 25.6]
spiegel_g = [31.0, 30.0, 34.0, 32.0, 32.0]'''

gegenstand_g = np.array([19.0, 19.0, 19.0, 19.0, 19.0])/100
kabs_g = np.array([26.5, 26.35, 26.4, 26.4, 26.45])/100
labs_g = np.array([26.6, 26.55, 26.55, 26.5, 26.6])/100
#spiegel_g = [31.0, 30.0, 34.0, 32.0, 32.0]

u_gegenstand_b = ufloat(19/100,1/2/2/np.sqrt(6)/1000)
u_kabs_b = ufloat(np.mean(kabs_b),np.std(kabs_b)*2.96)
u_labs_b = ufloat(np.mean(labs_b),np.std(labs_b)*2.96)
u_krel_b = -u_gegenstand_b+u_kabs_b
u_lrel_b = -u_gegenstand_b+u_labs_b

u_gegenstand_g = ufloat(19/100,1/2/2/np.sqrt(6)/1000)
u_kabs_g = ufloat(np.mean(kabs_g),np.std(kabs_g)*2.96)
u_labs_g = ufloat(np.mean(labs_g),np.std(labs_g)*2.96)
u_krel_g = -u_gegenstand_g+u_kabs_g
u_lrel_g = -u_gegenstand_g+u_labs_g


print(u_krel_b)
print(u_lrel_b)
print(u_krel_g)
print(u_lrel_g)

print('f für Linse b:')
print((u_krel_b+u_lrel_b)/2)
print('f für Linse g:')
print((u_krel_g+u_lrel_g)/2)