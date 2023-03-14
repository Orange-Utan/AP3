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



gamma1 = ufloat(8.4, 0.05/(2*np.sqrt(6)))
gamma2 = ufloat(128, 0.05/(2*np.sqrt(6)))
alpha = gamma2-gamma1

"""orange (135, 2 ± 0, 01) (184, 0 ± 0, 01)
Grün (135, 0 ± 0, 01) (184, 0 ± 0, 01)
Blau (133, 3 ± 0, 01) (184, 0 ± 0, 01)
Energiesparlampe Rot (358, 0 ± 0, 01) (310, 0 ± 0, 01)
Energiesparlampe Grün (357, 8 ± 0, 01) (309, 2 ± 0, 01)"""

orange = (ufloat(184.0,0.01)-ufloat(135.2,0.01))*2*np.pi/360
grün = (ufloat(184.0,0.01)-ufloat(135.0,0.01))*2*np.pi/360
blau = (ufloat(184.0,0.01) -ufloat(133.3,0.01))*2*np.pi/360
e_rot =( ufloat(358.0,0.01) -ufloat(310.0,0.01))*2*np.pi/360
e_grün = (ufloat(357.8,0.01) - ufloat(309.2,0.01))*2*np.pi/360

"""print(orange)
print(grün)
print(blau)
print(e_rot)
print(e_grün)"""

"""print(gamma1)
print(gamma2)
print(alpha)
print(alpha/2)"""


def n(delta):
    epsilon = ufloat(59.8,0.007)*2*np.pi/360
    return unumpy.sin((delta+epsilon)/2)/unumpy.sin(epsilon/2)



print(n(orange))
print(n(grün))
print(n(blau))
print(n(e_rot))
print(n(e_grün))

literatur = uarray([579.07,546.07, 435.83],0 )
n_lamda = uarray([nominal_values(n(orange)),nominal_values(n(grün)),nominal_values(n(blau))],[std_devs(n(orange)),std_devs(n(grün)),std_devs(n(blau))])


fig, ax = plt.subplots()


ax.errorbar(
        nominal_values(literatur),
        nominal_values(n_lamda),
        label = r'n aufgetragen gegen $\lambda$',
        color = 'purple',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        #xerr=std_devs(P_List),
        yerr=std_devs(n_lamda)
        )
ax.set_xlabel("Wellenlänge in nm")
ax.set_ylabel("n($\lambda$)")

def fit(x,a,b):
    return a*x+b


popt, pcov = curve_fit(fit, xdata=nominal_values(literatur), ydata=nominal_values(n_lamda))
ax.plot(np.linspace(390,650,1000),fit(np.linspace(390,650,1000),popt[0],popt[1]),
        'green',
        label='Ausgleichsgerade, $n(\lambda)=-1,39\cdot10^{-4}\cdot \lambda+1,71$')
print(np.sqrt(pcov))
print(popt)
plt.legend()
plt.show()