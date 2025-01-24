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
import uncertainties as uc
import uncertainties.umath as umath
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import generalFunctions as gf






jahr = []

for i in range(0,29):
        jahr.append(2010 + i/2)

anzahlResos = [4,3,3,4,0,4,3,4,3,4,1,4,6,12,13,11,12,13,8,6,12,3,8,9,3,8,11,17,12]


fig, ax = plt.subplots()
ax.errorbar(
        x=jahr,
        y=anzahlResos,
        #label = r'',
        color = 'g',
        linestyle='',
        marker='o',
        capsize=1.5,
        #elinewidth=1.2,
        #yerr=std_devs(gang_u),
        #xerr=std_devs(alpha_u)
        )
ax.errorbar(
        x=[2024.5],
        y=[22],
        #label = r'',
        color = 'r',
        linestyle='',
        marker='o',
        capsize=1.5,
        #elinewidth=1.2,
        #yerr=std_devs(gang_u),
        #xerr=std_devs(alpha_u)
        )

x_lin = np.linspace(2010,2026,10)

def func(x,a,b):
        return a * (x) + b
        #return a*x**2 + b * x + c

def funcXSq(x,a,b,c):
        return a * (x) + b+c
        #return a*x**2 + b * x + c
        #return a * 2.71**(b*(x-2010)) + c

popt, pcov = curve_fit(funcXSq, xdata=jahr, ydata=anzahlResos)

"""ax.plot(x_lin,func(x_lin,popt[0],popt[1]),
        'purple',
        label='Linearer Fit')"""


"""ax.plot(np.linspace(2010,2026,10),func(np.linspace(2010,2026,10),popt[0]+np.sqrt(pcov[0][0]),popt[1]+np.sqrt(pcov[1][1])),
        'blue',
        label='Unsicherheit')
ax.plot(np.linspace(2010,2026,10),func(np.linspace(2010,2026,10),popt[0]-np.sqrt(pcov[0][0]),popt[1]-np.sqrt(pcov[1][1])),
        'blue',
        label='Unsicherheit')"""

#a_fit, b_fit = uc.correlated_values(popt, pcov)
a_fit, b_fit, c_fit = uc.correlated_values(popt, pcov)


#fit_result = funcXSq(x_lin, a_fit, b_fit)
fit_result = funcXSq(x_lin, a_fit, b_fit, c_fit)

fit_result_val = unp.nominal_values(fit_result)
fit_result_std = unp.std_devs(fit_result)

plt.plot(x_lin, fit_result_val, c="purple", lw=1, label="Fit") # Plotting
plt.fill_between(x_lin, fit_result_val - fit_result_std, fit_result_val + fit_result_std, color="k", alpha=0.2, label="1$\sigma$ confidence interval")

ax.set_xlabel('Jahr')
ax.set_ylabel('# Beschlüsse')

plt.legend()
plt.show()

