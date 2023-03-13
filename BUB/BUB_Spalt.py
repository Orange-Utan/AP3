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


l1_links = uarray([0,0.26, 0.49, 0.66, 0.9, 1.13, 1.35, 1.56, 1.77, 1.95, 2.2],)
l1_rechts = uarray([0,0.29, 0.48, 0.68, 0.94, 1.15, 1.35, 1.58, 1.78, 1.97, 2.21],)

l2_links =uarray([0,0.44, 0.9, 1.34, 1.79, 2.21, 2.63, 3.09, 3.56, 3.92, 4.38, 4.8],)
l2_rechts = uarray([0,0.47, 0.91, 1.35, 1.76, 2.27, 2.65, 3.08, 3.57, 4.0, 4.42, 4.91],)

l3_links = uarray([0,0.78, 1.49, 2.21, 2.96, 3.78, 4.41, 5.17, 5.77, 6.56],)
l3_rechts = uarray([0,0.78, 1.53, 2.23, 3.0, 3.74, 4.43, 5.22, 6.02, 6.61],)


