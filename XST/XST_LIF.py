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
import tabulate
from tabulate import tabulate
from matplotlib.ticker import MultipleLocator, AutoMinorLocator



beta = uarray([8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0],np.sqrt(0.05**2+0.1**2))
r0=uarray([42.0, 42.3, 40.3, 51.0, 43.5, 40.0, 47.3, 41.5, 46.3, 53.8, 86.0, 117.5, 115.0, 63.5, 51.8, 50.3, 46.0, 46.0, 41.8, 44.8, 55.0, 144.8, 321.8, 373.3, 177.0, 59.8, 37.8, 37.5, 37.5, 37.0, 32.8],0)
r1 = uarray([89.8, 91.5, 93.8, 83.8, 84.3, 91.8, 84.5, 92.5, 88.8, 116.8, 177.8, 250.8, 214.5, 132.3, 102.0, 90.8, 96.8, 90.0, 92.8, 100.0, 118.5, 295.3, 625.8, 691.0, 352.0, 117.3, 93.8, 72.8, 73.0, 67.8, 71.5],0)
r2 = uarray([143.5, 140.3, 135.8, 142.0, 136.5, 136.3, 127.5, 128.8, 135.5, 183.0, 252.0, 343.8, 336.5, 197.5, 139.5, 137.3, 136.0, 145.3, 131.0, 139.3, 165.5, 466.0, 923.0, 975.3, 515.3, 177.3, 122.0, 109.8, 116.5, 104.0, 111.8],0)
r3 =uarray([183.0, 185.5, 182.0, 165.8, 186.0, 185.0, 178.3, 168.3, 173.0, 236.3, 336.5, 450.3, 430.3, 259.3, 178.0, 179.3, 178.8, 182.0, 176.8, 180.8, 230.8, 576.5, 1151.3, 1294.3, 678.3, 240.5, 161.5, 147.5, 154.5, 140.0, 137.3],0)
r4 =uarray([220.5, 231.0, 222.8, 223.3, 229.3, 199.0, 204.3, 222.3, 226.8, 265.3, 413.5, 547.8, 542.5, 331.5, 244.0, 237.5, 223.0, 231.5, 217.0, 233.0, 279.3, 698.8, 1378.5, 1566.8, 835.0, 283.5, 189.0, 182.0, 180.0, 182.5, 168.8],0)
r5=uarray([284.8, 272.3, 276.8, 263.3, 238.8, 251.5, 251.0, 266.8, 265.3, 341.0, 492.8, 630.5, 622.5, 403.3, 281.3, 269.8, 254.3, 260.5, 267.5, 283.8, 338.5, 847.5, 1617.8, 1778.3, 988.0, 354.5, 238.5, 224.3, 217.5, 211.0, 218.0],0)
r6=uarray([313.8, 298.3, 292.3, 300.5, 291.5, 305.0, 305.0, 287.3, 303.8, 375.8, 561.3, 756.5, 738.0, 459.3, 307.0, 299.8, 301.3, 294.8, 293.0, 305.5, 387.8, 966.0, 1858.3, 2015.5, 1170.0, 410.5, 257.8, 246.0, 242.3, 242.5, 221.3],0)
r7=uarray([340.3, 335.5, 339.3, 350.3, 348.8, 340.8, 332.3, 335.3, 358.3, 424.0, 602.0, 818.0, 821.3, 508.3, 360.0, 333.8, 332.0, 341.8, 340.5, 352.0, 422.0, 1052.8, 1977.5, 2261.3, 1343.5, 456.5, 296.8, 295.0, 285.8, 280.8, 254.3],0)
r8 = uarray([378.8, 373.3, 383.5, 379.3, 367.5, 372.3, 368.3, 351.5, 376.3, 478.8, 708.3, 909.0, 922.0, 585.3, 407.0, 396.5, 376.0, 375.0, 380.8, 394.8, 480.8, 1143.8, 2195.0, 2505.3, 1555.5, 534.0, 368.0, 308.0, 310.8, 309.5, 301.3],0)
r9= uarray([418.0, 436.0, 419.3, 411.8, 421.5, 408.5, 405.0, 386.8, 417.3, 517.3, 749.0, 978.8, 987.0, 627.5, 419.3, 394.8, 404.8, 415.5, 419.3, 440.0, 512.8, 1242.3, 2292.3, 2678.5, 1631.5, 605.5, 385.0, 355.0, 358.3, 333.3, 332.8],0)

"""maxima = []
rs = [r0,r1,r2,r3,r4,r5,r6,r7,r8,r9]

for r in rs:
        maxima.append(np.max(nominal_values(r)))

print(maxima)"""
maxima = uarray([373.3, 691.0, 975.3, 1294.3, 1566.8, 1778.3, 2015.5, 2261.3, 2505.3, 2678.5],np.array([373.3, 691.0, 975.3, 1294.3, 1566.8, 1778.3, 2015.5, 2261.3, 2505.3, 2678.5])*0.05)
stromI = uarray(np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])/1000,20*10**(-6))



fig,ax =plt.subplots()



ax.errorbar(
        nominal_values(maxima),
        nominal_values(stromI)*1000,
        label = r'Messungen bei Länge 1 = $(50,5 \pm 0,09)\,$cm',
        color = 'purple',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        yerr=std_devs(stromI),
        xerr= std_devs(maxima)
        )

def fit(x,a,b):

        return a*x+b

popt, pcov = curve_fit(fit, xdata=nominal_values(maxima), ydata=nominal_values(stromI)*1000)
ax.plot(np.linspace(300,2800,10000),fit(np.linspace(300,2800,10000),popt[0],popt[1]),
        'green',
        label='Zählrate aufgetragen gegen Strom, Fitkurve: Z=$3,88\cdot10^{-4}$I$-76,96\cdot10^{-3}$ ')

ax.set_xlabel("Zählrate")
ax.set_ylabel("Strom in mA")

table = [maxima,stromI]
print(tabulate(table, tablefmt="latex"))
print(np.sqrt(pcov))
print(popt)
plt.legend()
plt.show()