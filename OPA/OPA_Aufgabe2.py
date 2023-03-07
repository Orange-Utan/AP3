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


'''gegenstand_b = [17.0, 18.0, 20.0, 19.0, 19.0]
kabs_b = [27.0, 28.05, 30.1, 29.0, 28.9]
labs_b = [27.1, 28.2, 29.9, 29.2, 29.0]
spiegel_b = [40.0, 32.0, 34.0, 34.0, 34.0]'''


gegenstand_b = [19.0, 19.0, 19.0, 19.0, 19.0]
kabs_b = [29.0, 29.05, 29.1, 29.0, 28.9]
labs_b = [29.1, 29.2, 28.9, 29.2, 29.0]
#spiegel_b = [42.0, 33.0, 33.0, 34.0, 34.0]

'''gegenstand_g = [17.0, 16.1, 19.0, 15.5, 18.0]
kabs_g = [24.5, 23.45, 26.4, 22.9, 25.45]
labs_g = [24.6, 23.65, 26.55, 23.0, 25.6]
spiegel_g = [31.0, 30.0, 34.0, 32.0, 32.0]'''

gegenstand_g = [19.0, 19.0, 19.0, 19.0, 19.0]
kabs_g = [26.5, 26.35, 26.4, 26.4, 26.45]
labs_g = [26.6, 26.55, 26.55, 26.5, 26.6]
#spiegel_g = [31.0, 30.0, 34.0, 32.0, 32.0]

u_gegenstand_b = uarray(np.array(gegenstand_b)/100,1/2/2/np.sqrt(6)/1000)
u_kabs_b = uarray(np.array(kabs_b)/100,1/2/2/np.sqrt(6)/1000)
u_labs_b = uarray(np.array(labs_b)/100,1/2/2/np.sqrt(6)/1000)
#u_spiegel_b = uarray(np.array(spiegel_b)/100,1/2/2/np.sqrt(6)/1000)
u_krel_b = u_kabs_b-u_gegenstand_b
u_lrel_b = u_labs_b-u_gegenstand_b



u_gegenstand_g = uarray(np.array(gegenstand_g)/100,1/2/2/np.sqrt(6)/1000)
u_kabs_g = uarray(np.array(kabs_g)/100,1/2/2/np.sqrt(6)/1000)
u_labs_g = uarray(np.array(labs_g)/100,1/2/2/np.sqrt(6)/1000)
#u_spiegel_g = uarray(np.array(spiegel_g)/100,1/2/2/np.sqrt(6)/1000)
u_krel_g = u_kabs_g-u_gegenstand_g
u_lrel_g = u_labs_g-u_gegenstand_g




print(std_dev(gegenstand_g))



