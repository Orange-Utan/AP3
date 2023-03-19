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




beta_4bis8p5 = [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5]


r0_4bis6p5 = [26.4, 28.0, 23.1, 27.8, 28.0, 28.4, 26.5, 33.8, 33.5, 35.8, 36.0, 58.8, 86.6, 139.4, 189.6, 223.8, 254.8, 285.4, 297.8, 304.0, 319.5, 324.9, 325.1, 334.9, 341.3, 351.5]
r1_4p5bis7 = [19.4, 20.6, 18.9, 20.3, 22.0, 25.1, 24.5, 24.6, 24.3, 27.5, 45.0, 72.4, 116.9, 147.0, 175.3, 199.1, 208.9, 214.6, 237.8, 241.9, 251.1, 251.3, 270.4, 270.3, 264.9, 271.6]
r2_5bis7p5 = [13.4, 14.3, 15.1, 12.8, 15.1, 17.8, 17.3, 14.1, 16.8, 27.1, 43.4, 67.9, 97.4, 117.4, 132.0, 151.3, 172.3, 172.1, 177.4, 192.8, 209.5, 199.4, 210.6, 218.8, 215.6, 222.5]
r3_5p5bis8p5 = [11.75, 14.19, 14.88, 14.44, 14.25, 14.13, 14.5, 16.13, 23.44, 31.5, 58.31, 85.31, 113.06, 124.81, 143.88, 161.13, 173.06, 174.19, 191.0, 196.81, 200.63, 202.06, 217.0, 223.69, 215.81, 228.69, 222.38, 225.31, 231.88, 226.94, 235.19]
r4_6bis8p5 = [9.5, 8.75, 9.81, 8.88, 9.56, 9.63, 10.94, 11.69, 15.0, 27.81, 43.88, 71.38, 85.94, 103.63, 114.31, 128.5, 133.75, 142.88, 153.38, 155.25, 167.88, 166.69, 170.44, 177.5, 180.94, 181.56]
r5_6p5bis8p5 = [4.31, 5.5, 6.56, 5.69, 6.31, 7.25, 7.38, 6.25, 8.81, 14.19, 27.19, 41.38, 63.25, 75.5, 84.44, 95.31, 104.0, 110.75, 120.81, 122.06, 130.88]

beta_4bis8p5_u = uarray(beta_4bis8p5,(0.05**2+0.1**2)**0.5)
r0_4bis6p5_u = uarray(r0_4bis6p5,np.array(r0_4bis6p5)*0.05)
r1_4p5bis7_u = uarray(r1_4p5bis7,np.array(r1_4p5bis7)*0.05)
r2_5bis7p5_u = uarray(r2_5bis7p5,np.array(r2_5bis7p5)*0.05)
r3_5p5bis8p5_u = uarray(r3_5p5bis8p5,np.array(r3_5p5bis8p5)*0.05)
r4_6bis8p5_u = uarray(r4_6bis8p5,np.array(r4_6bis8p5)*0.05)
r5_6p5bis8p5_u = uarray(r5_6p5bis8p5,np.array(r5_6p5bis8p5)*0.05)

r_u = [r0_4bis6p5_u,r1_4p5bis7_u,r2_5bis7p5_u,r3_5p5bis8p5_u,r4_6bis8p5_u,r5_6p5bis8p5_u]
beta_u = [beta_4bis8p5_u[0:26],beta_4bis8p5_u[5:31],beta_4bis8p5_u[10:36],beta_4bis8p5_u[15:46],beta_4bis8p5_u[20:46],beta_4bis8p5_u[25:46]]

def func(x, a, b):
    return a*x + b

fit_r_u = [r0_4bis6p5_u[10:17+1],r1_4p5bis7_u[9:16+1],r2_5bis7p5_u[8:16+1],r3_5p5bis8p5_u[8:16+1],r4_6bis8p5_u[8:18+1],r5_6p5bis8p5_u[8:20+1]]
fit_beta_u = [beta_4bis8p5_u[10:17+1],beta_4bis8p5_u[5+9:16+5+1],beta_4bis8p5_u[10+8:10+16+1],beta_4bis8p5_u[15+8:15+16+1],beta_4bis8p5_u[20+8:20+18+1],beta_4bis8p5_u[25+8:25+20+1]]



fig,ax =plt.subplots()
for i in range(0,6):
        ax.errorbar(
                nominal_values(beta_u[i]),
                nominal_values(r_u[i]),
                label = r'Messung ' + str(i+1),
                #color = 'purple',
                #linestyle='',
                marker='.',
                #capsize=1.5,
                elinewidth=0.5,
                xerr=std_devs(beta_u[i]),
                yerr= std_devs(r_u[i])
                )
        popt, pcov = curve_fit(func, xdata=nominal_values(fit_beta_u[i]), ydata=nominal_values(fit_r_u[i]))
        ax.plot(np.linspace(4, 8.5, 10),
                func(np.linspace(4, 8.5, 10), popt[0], popt[1]),
                label='Fit, Messung ' + str(i+1))
        print('Messung ' + str(i+1) + ' popt:' + str(popt))
        print('Messung ' + str(i+1) + ' pcov:' + str(np.sqrt(pcov)))
        print('Messung ' + str(i+1) + ' NS:' + str(np.roots(popt)))

ax.set_ylim(-5,400)
plt.legend()
plt.show()