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
import generalFunctions as gf
from matplotlib.ticker import MultipleLocator, AutoMinorLocator



Cs_chan = ufloat(233.3,6.2)
Cs_E = 662

Co_chan = [ufloat(401.4,7),ufloat(455.0,6.7)]
Co_2_chan = ufloat(851,10)
Co_E = [1173,1333]


Na_chan = ufloat(185.8,5.6)
Na_2_chan = ufloat(445.6,7)
Na_3_chan = ufloat(627.0,8.1)
Na_E = 1275


fitList_x = [Cs_chan,Co_chan[0],Co_chan[1],Na_2_chan,Na_chan,Na_3_chan,Co_2_chan]
fitList_y = [Cs_E,Co_E[0],Co_E[1],Na_E,511,Na_E+511,Co_E[0]+Co_E[1]]

fig, ax = plt.subplots()

ax.errorbar(
        x=nominal_values(Cs_chan),
        y=nominal_values(Cs_E),
        label = r'Cs-137',
        linestyle='-',
        color = 'm',
        marker='',
        capsize=1.5,
        #yerr=std_devs(gang_u),
        xerr=std_devs(Cs_chan)
        )
for i in range(0,2):
    ax.errorbar(
            x=nominal_values(Co_chan[i]),
            y=nominal_values(Co_E[i]),
            label = r'Co-60',
            linestyle='-',
            color = 'g',
            marker='',
            capsize=1.5,
            #yerr=std_devs(gang_u),
            xerr=std_devs(Co_chan[i])
            )
ax.errorbar(
            x=nominal_values(Co_2_chan),
            y=nominal_values(Co_E[0]+Co_E[1]),
            label = r'Co-60, beide Quanten gleichzeitig',
            linestyle='-',
            color = 'aqua',
            marker='',
            capsize=1.5,
            #yerr=std_devs(gang_u),
            xerr=std_devs(Co_chan[i])
            )

ax.errorbar(
            x=nominal_values(Na_2_chan),
            y=nominal_values(Na_E),
            label = r'Na-22',
            linestyle='-',
            color = 'orange',
            marker='',
            capsize=1.5,
            #yerr=std_devs(gang_u),
            xerr=std_devs(Na_chan)
            )

ax.errorbar(
            x=nominal_values(Na_chan),
            y=511,
            label = 'Ruheenergie des Elektrons beim Aussenden \nder $\gamma$-Quanten beim $\\beta^+$-Zerfalls des Na-22',
            linestyle='-',
            color = 'red',
            marker='',
            capsize=1.5,
            #yerr=std_devs(gang_u),
            xerr=std_devs(Na_chan)
            )
ax.errorbar(
            x=nominal_values(Na_3_chan),
            y=511+Na_E,
            label = r'Na-22, beide Quanten gleichzeitig',
            linestyle='-',
            color = 'xkcd:rosy pink',
            marker='',
            capsize=1.5,
            #yerr=std_devs(gang_u),
            xerr=std_devs(Na_chan)
            )

def func(x,a,b):
    return a*x +b


popt, pcov = curve_fit(func, xdata=nominal_values(fitList_x), ydata=nominal_values(fitList_y))
ax.plot(np.linspace(1,1024,5),
        func(np.linspace(1,1024,5),*popt),
        linewidth=0.7,
        label='Kalibrierungs Fit'
        )
print(popt)

ax.set_xlabel('Channel', fontsize= 16)
ax.set_ylabel('Energie [keV]', fontsize= 16)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.legend(loc=1, prop={'size': 16})

plt.legend(fontsize= 13)
plt.show()