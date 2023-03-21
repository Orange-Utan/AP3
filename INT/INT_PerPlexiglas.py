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
import  generalFunctions as gf

dicke = 9.7/1000
nullpunkt = ufloat(4.6,0.05)

mess1 =np.array([4.13, 3.95, 3.8, 3.65, 3.52])
max1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0] )
mess2 = np.array([4.92, 5.13, 5.32, 5.44, 5.0])
max2 = np.array( [-1.0, -2.0, -3.0, -4.0, -5.0])
mess3 = np.array([3.68, 3.34, 3.1, 2.9])
max3= np.array([5.0, 10.0, 15.0, 20.0])
mess4 = np.array([5.28, 5.55, 5.83, 6.03, 6.25, 6.48, 6.6, 6.79, 6.98, 7.11, 7.26, 7.41, 7.54, 7.67, 7.78, 7.9, 8.0])
max4 =np.array( [-5.0, -10.0, -15.0, -20.0, -25.0, -30.0, -35.0, -40.0, -45.0, -50.0, -55.0, -60.0, -65.0, -70.0, -75.0, -80.0, -85.0])

messpos= [4.13, 3.95, 3.8, 3.65, 3.52,3.68, 3.34, 3.1, 2.9]
maxpos = [1.0, 2.0, 3.0, 4.0, 5.0,5.0, 10.0, 15.0, 20.0]
messneg =[4.92, 5.13, 5.32, 5.44, 5.0,5.28, 5.55, 5.83, 6.03, 6.25, 6.48, 6.6, 6.79, 6.98, 7.11, 7.26, 7.41, 7.54, 7.67, 7.78, 7.9, 8.0]
maxneg = [-1.0, -2.0, -3.0, -4.0, -5.0, -5.0, -10.0, -15.0, -20.0, -25.0, -30.0, -35.0, -40.0, -45.0, -50.0, -55.0, -60.0, -65.0, -70.0, -75.0, -80.0, -85.0]

mess = [8.,   7.9 , 7.78, 7.67, 7.54, 7.41, 7.26, 7.11, 6.98, 6.79, 6.6,  6.48, 6.25, 6.03,5.83 ,5.55 ,5.28 ,5., 5.44, 5.32, 5.13, 4.92,4.6,4.13, 3.95, 3.8, 3.65, 3.52,3.68, 3.34, 3.1, 2.9]
max = [-85., -80., -75. ,-70., -65., -60., -55., -50., -45. ,-40., -35. ,-30., -25. ,-20.,-15., -10.,  -5.  ,-5.,  -4.  ,-3.,  -2. , -1.,0,1.0, 2.0, 3.0, 4.0, 5.0,5.0, 10.0, 15.0, 20.0]

us_mess = 0.05
us_max = [1, 1,1 ,1, 1, 1., 1,1, 1 ,1, 1 ,1, 1 ,1,1, 1,  1  ,0.5,  0.5  ,0.5,  0.5, 0.5,0,0.5, 0.5, 0.5, 0.5, 0.5,1, 1, 1, 1]



mess_u = uarray(mess,us_mess/(2*np.sqrt(6)))/1000
messnp = mess_u-nullpunkt/1000
max_u = abs(uarray(max,us_max/(2*np.sqrt(6))))
alpha_u = unumpy.arctan(messnp/(28/1000))
#print(alpha_u)
lamda = ufloat(532,1)/(10**(9))
gang_u = max_u*lamda
def tabularX():
    spalte = dict()
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Maxima" + "}"] = max_u
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Schraubenstellung in mm zum Nullpunkt" + "}"] = mess_u*1000
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Schraubenstellung in mm" + "}"] = messnp * 1000
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Winkel $\alpha$ im Bogenmaß" + "}"] = alpha_u
    textabular = f"|{'c|' * len(sorted(spalte))}"
    # texheader = " & " + " & ".join(headers) + "\\\\"
    # texheader = " & ".join(headers) + "\\\\"
    texheader = " & ".join(spalte.keys())
    texheader = texheader + ' &'
    # texdata = "\\hline\n"
    texdata = ""
    for i in range(0,len(mess)):
        texdata += '\\hline'
        for label in sorted(spalte):
            texdata += str(gf.ufloatToTexStr(spalte[label][i])) + ' & '

    print("\\begin{table}[]")
    print("\\centering")
    print("\\resizebox{\columnwidth}{!}{")
    print("\\begin{tabular}{" + textabular + "}")
    print("\\hline")
    print(texheader)
    print(texdata, end="")
    print("\\hline")
    print("\\end{tabular}")
    print("}")
    print("\\caption{Messergebnisse an der Plexiglasscheibe}")
    print("\\label{tab:Plexi}")
    print("\\end{table}")


fig, ax = plt.subplots()
ax.errorbar(
        y=nominal_values(gang_u),
        x=nominal_values(alpha_u),
        label = r'Gangunterschied gegen den Winkel aufgetragen',
        color = 'blue',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        yerr=std_devs(gang_u),
        xerr=std_devs(alpha_u)
        )

def func(alpha, n):
    return 2*dicke*(1-n-np.cos(alpha)+(n**2-np.sin(alpha)**2)**0.5)

#def func(alpha, n)

popt3, pcov3 = curve_fit(func, ydata=nominal_values(gang_u), xdata=nominal_values(alpha_u),p0=1.49)
ax.plot(np.linspace(-0.06, 0.125, 100), func(np.linspace(-0.06, 0.125, 100), popt3[0]),
        'red',
        label=r'Fit, $n= 1.487\pm 0.009$')

print(popt3)
print(np.sqrt(pcov3))


ax.set_ylabel(r"Gangunterschied $\Delta s= N \cdot \lambda$ in m")
ax.set_xlabel(r"Winkel $\alpha$")
plt.legend()
plt.show()


