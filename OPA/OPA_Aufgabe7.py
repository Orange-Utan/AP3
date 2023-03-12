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

f1strich = (ufloat(7.49,0.019)/100+ufloat(7.26,0.033)/100)/2
print(f1strich)
fges = ufloat(12.6,0.25)/100
t = 3/100
h = ufloat(3.3, 0.6)/100

f2strich = (t-f1strich)/(-f1strich/fges+1)
print(f2strich*100)


#Abbe


f1strich = (ufloat(7.49,0.019)/100+ufloat(7.26,0.033)/100)/2
print(f1strich)
fges = (ufloat(9.6,2.3)/100+ufloat(14.8,1.8)/100)/2
print(fges)
t = 3/100
#h = (ufloat(27.9,1.8)/100-ufloat(26.8,6.9)/100)/2

f2strich = (t-f1strich)/(-f1strich/fges+1)
print(f2strich*100)
