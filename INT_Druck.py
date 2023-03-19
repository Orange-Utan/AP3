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



mess1 = uarray([0.0, 0.05, 0.1, 0.18, 0.24, 0.3, 0.35, 0.4, 0.48, 0.52, 0.59, 0.64, 0.71, 0.76, 0.82],0.01/2*np.sqrt(6))
mess2 = uarray([0.0, 0.06, 0.1, 0.16, 0.22, 0.28, 0.34, 0.38, 0.44, 0.5, 0.56, 0.63, 0.69, 0.74, 0.8],0.01/2*np.sqrt(6))
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
    for i in range(0,len(spalte)-1):
        texdata += '\\hline'
        for label in sorted(spalte):
            texdata += str(spalte[label][i]) + ' & '

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
tabularX()