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


gegenstand_b = [17.0, 18.0, 20.0, 19.0, 19.0]
krel_b = [27.0, 28.05, 30.1, 29.0, 28.9]
lrel_b = [27.1, 28.2, 29.9, 29.2, 29.0]
Spiegel_b = [40.0, 32.0, 34.0, 34.0, 34.0]

gegenstand_g = [17.0, 16.1, 19.0, 15.5, 18.0]
krel_g = [24.5, 23.45, 26.4, 22.9, 25.45]
lrel_g = [24.6, 23.65, 26.55, 23.0, 25.6]
Spiegel_g = [31.0, 30.0, 34.0, 32.0, 32.0]



