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

#Ungenau: Messkala 0,5mm,Scharfstellen rechts 1mm,Scharfstellen links 3mm

#alles in m
gegenstand = 19.0/100

linksabs_b = np.array([31.4, 31.2, 30.9, 31.0, 30.9])/100
rechtsabs_b = np.array([72.8, 72.6, 72.9, 73.05, 73.0])/100
schirm_b = 85/100

linksabs_g = np.array([27.5, 28.0, 27.8, 27.7, 28.0])/100
rechtsabs_g = np.array([58.0, 57.9, 58.1, 57.95, 57.9])/100
schirm_g = 67/100

u_gegenstand = ufloat(gegenstand,1/2/2/np.sqrt(6)/1000)

u_linksabs_b = ufloat(np.mean(linksabs_b),np.std(linksabs_b)*0.51)
u_rechtsabs_b = ufloat(np.mean(rechtsabs_b),np.std(rechtsabs_b)*0.51)
u_schirm_b = ufloat(schirm_b,1/2/2/np.sqrt(6)/1000)

u_linksabs_g = ufloat(np.mean(linksabs_g),np.std(linksabs_g)*0.51)
u_rechtsabs_g = ufloat(np.mean(rechtsabs_g),np.std(rechtsabs_g)*0.51)
u_schirm_g = ufloat(schirm_g,1/2/2/np.sqrt(6)/1000)

f_b = 1/4*((u_schirm_b-u_gegenstand)-((u_rechtsabs_b-u_linksabs_b)**2)/(u_schirm_b-u_gegenstand))
print(f_b)
f_g = 1/4*((u_schirm_g-u_gegenstand)-((u_rechtsabs_g-u_linksabs_g)**2)/(u_schirm_g-u_gegenstand))
print(f_g)
