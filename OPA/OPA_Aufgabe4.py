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

#Unsicherheiten Autoko: Messkala 0.5, Scharfstellen 1mm, Bessel: Messkala 0,5mm,Scharfstellen rechts 1mm,Scharfstellen links 3mm
#alles in cm
gegenstand = 13

autoko0 = [30.3, 30.8, 30.7, 30.5, 30.5]
autoko180 = [24.1, 24.0, 23.6, 23.9, 24.0]
autospiegel = 40

bessellinks = [33.2, 34.3, 33.8, 33.9, 33.2]
besselrechts = [81.0, 80.8, 80.9, 80.7, 81.1]
besselschirm = 95


