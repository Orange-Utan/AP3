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


 # Unsicherheiten : 0,5mm maxima in mm , verzählt 5 maxima-5%, Luftwirbel 0,5%
nmax = np.array([30,28,28.5,31])
nmax_u = uarray(nmax,np.sqrt((0.5/2*np.sqrt(6))**2+(nmax*0.05)**2+(nmax*0.005)**2))
lamda = ufloat(532,1)

print(nmax_u)


