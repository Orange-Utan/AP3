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
gegenstand = 13/100

autoko0 = np.array([30.3, 30.8, 30.7, 30.5, 30.5])/100
autoko180 = np.array([24.1, 24.0, 23.6, 23.9, 24.0])/100
autospiegel = 40/100
bessellinks = np.array([33.2, 34.3, 33.8, 33.9, 33.2])/100
besselrechts = np.array([81.0, 80.8, 80.9, 80.7, 81.1])/100
besselschirm = 95/100


u_gegenstand = ufloat(gegenstand,1/2/2/np.sqrt(6)/1000)

u_autoko_0 = ufloat(np.mean(autoko0),np.std(autoko0)*0.51)
u_autoko_180 = ufloat(np.mean(autoko180),np.std(autoko180)*0.51)
u_autospiegel = ufloat(autospiegel,1/2/2/np.sqrt(6)/1000)

u_bessellinks = ufloat(np.mean(bessellinks),np.std(bessellinks)*0.51)
u_besselrechts = ufloat(np.mean(besselrechts),np.std(besselrechts)*0.51)
u_besselschirm = ufloat(besselschirm,1/2/2/np.sqrt(6)/1000)

e = u_besselschirm-u_gegenstand
k = u_autoko_0-u_gegenstand
l = u_autoko_180-u_gegenstand
d = u_besselrechts-u_bessellinks

f = 0.5*((e-k-l)**2-d**2)**0.5
h = k+l-((e-k-l)**2-d**2)**0.5


print(e*100)
print(k*100)
print(l*100)
print(d*100)
print(f*100)
print(h*100)






