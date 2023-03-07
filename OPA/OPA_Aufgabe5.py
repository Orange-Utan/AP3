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
rechts= np.array([128.4, 122.6, 117.6, 112.5, 107.4, 102.0, 96.9, 91.8, 86.1, 79.9, 75.4])/100
geggroesserechts = 25/100
bildGrRechts = np.array([2.25, 2.5, 3.0, 2.5, 4.0, 4.0, 4.5, 4.5, 5.5, 7.0, 7.5])/1000
ubildrechts = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.5, 0.7])/1000

