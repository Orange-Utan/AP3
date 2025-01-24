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
import generalFunctions as gf





def n(t):
    lam = np.log(2)/(2.6*365*24*60*60)
    N0 = lam/333
    return N0*np.exp(-lam*t)

def e(t):
    e0 = 662 *1000 *0.85
    return 7/100 * e0 * (n(0)-n(t))


print(e(365*24*60*60)/70)