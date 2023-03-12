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


f1 = (ufloat(7.49,0.019)/100+ufloat(7.26,0.033)/100)/2
t = 3/100

delta = t + f1 - 10

z = f1*t/delta*100

print(z)

z = 10*t/delta*100

print(z)

#zstrich = f2strich*t/delta