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


length = ufloat(4.96,0.005)/100
lamda = lamda = ufloat(532,1)/(10**(9))
mess1 =-uarray([0.0, 0.05, 0.1, 0.18, 0.24, 0.3, 0.35, 0.4, 0.48, 0.52, 0.59, 0.64, 0.71, 0.76, 0.82],0.01/2*np.sqrt(6))
mess2 =-uarray([0.0, 0.06, 0.1, 0.16, 0.22, 0.28, 0.34, 0.38, 0.44, 0.5, 0.56, 0.63, 0.69, 0.74, 0.8],0.01/2*np.sqrt(6))
max = uarray([0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0],1/2*np.sqrt(6))

mittelnorm = []
mittelstd = []

j=0
for i in range(15):
    m = uarray( [nominal_values(mess1[j]),nominal_values(mess2[j])],0.01/2*np.sqrt(6))
    w = gf.weightedAverage(m)
    mittelnorm.append(nominal_values(w))
    mittelstd.append(std_devs(w))
    j+=1



mittel = uarray(mittelnorm,mittelstd)
#print(mittel)


def tabularX():
    spalte = dict()
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Maxima" + "}"] = max
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Messung 1" + "}"] = mess1
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Messung 2" + "}"] = mess2
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Mittelwert" + "}"] =mittel

    textabular = f"|{'c|' * len(sorted(spalte))}"
    # texheader = " & " + " & ".join(headers) + "\\\\"
    # texheader = " & ".join(headers) + "\\\\"
    texheader = " & ".join(spalte.keys())
    texheader = texheader + ' &'
    # texdata = "\\hline\n"
    texdata = ""


    for i in range(0,len(spalte.values())-1):
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
    print("\\caption{Berücksichtigte Ungenauigkeiten}")
    print("\\label{tab:Ungenauigkeiten}")
    print("\\end{table}")

def brech(N):
    return -((N+1/2)*lamda/(2*length))

fig, ax = plt.subplots()
ax.errorbar(
        nominal_values(mess1),
        nominal_values(brech(max)),
        label = r'Messreihe 1',
        color = 'blue',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        xerr=std_devs(mess1),
        yerr=std_devs(brech(max))
        )
ax.errorbar(
        nominal_values(mess2),
        nominal_values(brech(max)),
        label = r'Messreihe 2',
        color = 'green',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        xerr=std_devs(mess2),
        yerr=std_devs(brech(max))
        )
ax.errorbar(
        nominal_values(mittel),
        nominal_values(brech(max)),
        label = r'Mittelwert',
        color = 'red',
        linestyle='',
        marker='.',
        capsize=1.5,
        #elinewidth=1.2,
        xerr=std_devs(mittel),
        yerr=std_devs(brech(max))
        )

Temp=295.7
def func(p,a,b):
    return a*p+b


popt3, pcov3 = curve_fit(func, xdata=nominal_values(mittel), ydata=nominal_values(brech(max)))
ax.plot(np.linspace(-1, 0, 100), func(np.linspace(-1, 0, 100), popt3[0],popt3[1]),
        'red',
        label='Fit an den Mittelwert: $\Delta \, n = 2,76\cdot 10^{-4} \cdot \Delta\, p + 4,36 \cdot 10^{-6}$')

print(popt3)
print(np.sqrt(pcov3))
ax.set_xlabel("$\Delta$p in bar")
ax.set_ylabel(r"$\Delta$n")
plt.legend()
plt.show()

