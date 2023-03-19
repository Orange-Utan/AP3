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


#test = uarray([1,2,3],[0.1,0.2,0.3])

def weightedAverage(werte): # werte ist ein uarray
    # nominal value
    w = []
    for x in werte:
        w.append(1/std_devs(x)**2)
    wSum = 0
    for y in w:
        wSum += y
    sumZahler = 0
    for i in range(0,len(werte)):
        sumZahler += w[i] * nominal_values(werte[i])
    nomWeighAvg = sumZahler/wSum

    #u_int
    u_int = (1/(wSum))**0.5

    #u_ext
    n = len(werte)
    extZahler = 0
    for j in range(0,n):
        extZahler += w[j] * (nominal_values(werte[j])-nomWeighAvg)**2
    u_ext = (extZahler/(n-1)/wSum)**0.5
    u = 0
    if u_int > u_ext:
        u = u_int
    else:
        u = u_ext
    return ufloat(nomWeighAvg,u)

def ufloatToTexStr(uf):
    ufloat = '{:.2u}'.format(uf)
    ufloat = str(ufloat)
    ufloat = ufloat.replace('+/-', ' \pm ')
    ufloat = "$" + ufloat + "$"
    if ufloat.__contains__('e'):
        ufloat = ufloat.replace('e', '\cdot 10^{')
        ufloat = ufloat.replace('+', '')
        ufloat = ufloat + "}"
    else:
        ufloat = ufloat
    return ufloat.replace('.', ',')
def tabularXY():
    headers_temp = ["", r"$2 \cdot \beta$ 1.Ordnung", r"$2 \cdot \alpha$ 1.Ordnung", r"$2 \cdot \beta$ 2.Ordnung", r"$2 \cdot \alpha$ 2.Ordnung", r"$2 \cdot \beta$ 3.Ordnung", r"$2 \cdot \alpha$ 3.Ordnung"]
    headers = []
    for i in range(0, len(headers_temp)):
        headers.append("\\cellcolor[HTML]{C0C0C0}\\textbf{" + headers_temp[i] + "}")
    data = dict()
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Linie für $0\,\si{\degree}$" + "}"] = [1, 2]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Linie für $180\,\si{\degree}$" + "}"] = [3, 2]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "Mittelwert" + "}"] = [1, 9]

    textabular = f"|c|{'c|' * len(headers)}"
    #texheader = " & " + " & ".join(headers) + "\\\\"
    texheader = " & ".join(headers) + "\\\\"
    #texdata = "\\hline\n"
    texdata = ""
    for label in sorted(data):
        #if label == "z":
        texdata += "\\hline\n"
        texdata += f"{label} & {' & '.join(map(str, data[label]))} \\\\\n"


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

def tabularX():
    spalte = dict()
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header1" + "}"] = [1, 2]
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header2" + "}"] = ['a', 'b']
    spalte["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Header3" + "}"] = ['f', 9]
    textabular = f"|{'c|' * len(sorted(spalte))}"
    # texheader = " & " + " & ".join(headers) + "\\\\"
    # texheader = " & ".join(headers) + "\\\\"
    texheader = " & ".join(spalte.keys())
    texheader = texheader + ' &'
    # texdata = "\\hline\n"
    texdata = ""
    for i in range(0,len(sorted(spalte)[0])-1):
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
