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
import generalFunctions as gf


betaFull = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9, 14.0, 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 15.0, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9, 16.0, 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.8, 16.9, 17.0, 17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9, 18.0, 18.1, 18.2, 18.3, 18.4, 18.5, 18.6, 18.7, 18.8, 18.9, 19.0, 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8, 19.9, 20.0, 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9, 21.0, 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7, 21.8, 21.9, 22.0, 22.1, 22.2, 22.3, 22.4, 22.5, 22.6, 22.7, 22.8, 22.9, 23.0, 23.1, 23.2, 23.3, 23.4, 23.5, 23.6, 23.7, 23.8, 23.9, 24.0, 24.1, 24.2, 24.3, 24.4, 24.5, 24.6, 24.7, 24.8, 24.9, 25.0]
beta2bis10 = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10.0]
beta18bis21 = [18.0, 18.1, 18.2, 18.3, 18.4, 18.5, 18.6, 18.7, 18.8, 18.9, 19.0, 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8, 19.9, 20.0, 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9, 21.0]

zeroDegreeNaCl = [6.0, 3.0, 2.0, 7.0, 5.0, 4.0, 4.0, 4.0, 4.0, 9.0, 3.0, 11.0, 19.0, 12.0, 13.0, 38.0, 129.0, 272.0, 435.0, 484.0, 584.0, 610.0, 653.0, 652.0, 696.0, 674.0, 655.0, 689.0, 625.0, 643.0, 612.0, 576.0, 520.0, 577.0, 566.0, 541.0, 485.0, 510.0, 482.0, 531.0, 508.0, 465.0, 509.0, 717.0, 980.0, 871.0, 676.0, 522.0, 459.0, 461.0, 614.0, 1140.0, 1888.0, 2002.0, 1137.0, 648.0, 469.0, 380.0, 344.0, 300.0, 309.0, 265.0, 275.0, 240.0, 233.0, 234.0, 217.0, 230.0, 238.0, 210.0, 206.0, 163.0, 191.0, 165.0, 159.0, 146.0, 133.0, 153.0, 136.0, 101.0, 122.0, 98.0, 114.0, 99.0, 107.0, 102.0, 91.0, 77.0, 90.0, 89.0, 83.0, 90.0, 102.0, 77.0, 95.0, 77.0, 88.0, 83.0, 91.0, 96.0, 69.0, 93.0, 68.0, 68.0, 85.0, 82.0, 89.0, 119.0, 172.0, 190.0, 173.0, 99.0, 82.0, 69.0, 72.0, 69.0, 73.0, 81.0, 59.0, 67.0, 65.0, 74.0, 72.0, 110.0, 313.0, 514.0, 437.0, 215.0, 110.0, 84.0, 55.0, 65.0, 65.0, 52.0, 64.0, 56.0, 58.0, 63.0, 42.0, 56.0, 46.0, 38.0, 55.0, 40.0, 44.0, 52.0, 54.0, 48.0, 38.0, 46.0, 44.0, 47.0, 38.0, 31.0, 32.0, 43.0, 35.0, 35.0, 38.0, 43.0, 33.0, 35.0, 38.0, 30.0, 28.0, 29.0, 32.0, 35.0, 25.0, 33.0, 28.0, 40.0, 22.0, 21.0, 24.0, 48.0, 54.0, 45.0, 37.0, 21.0, 32.0, 30.0, 22.0, 27.0, 22.0, 28.0, 16.0, 29.0, 22.0, 25.0, 19.0, 31.0, 23.0, 20.0, 25.0, 26.0, 25.0, 23.0, 23.0, 27.0, 51.0, 114.0, 126.0, 84.0, 56.0, 27.0, 21.0, 18.0, 14.0, 24.0, 16.0, 19.0, 23.0, 17.0, 17.0, 16.0, 21.0, 10.0, 13.0, 13.0, 16.0, 20.0, 12.0, 11.0, 16.0, 15.0, 18.0, 15.0, 14.0, 7.0, 10.0]
oneEightyNaCl = [2.0, 5.0, 3.0, 8.0, 7.0, 5.0, 7.0, 5.0, 7.0, 9.0, 6.0, 12.0, 16.0, 9.0, 24.0, 54.0, 105.0, 199.0, 328.0, 390.0, 479.0, 505.0, 515.0, 572.0, 582.0, 569.0, 535.0, 561.0, 516.0, 559.0, 487.0, 443.0, 441.0, 449.0, 499.0, 453.0, 431.0, 413.0, 414.0, 382.0, 412.0, 426.0, 388.0, 521.0, 714.0, 843.0, 713.0, 506.0, 399.0, 463.0, 507.0, 763.0, 1407.0, 1867.0, 1450.0, 797.0, 449.0, 364.0, 311.0, 272.0, 268.0, 261.0, 253.0, 253.0, 235.0, 250.0, 217.0, 179.0, 209.0, 187.0, 147.0, 157.0, 166.0, 137.0, 141.0, 123.0, 92.0, 118.0, 107.0, 106.0, 109.0]
NaCl18bis21 = [33.4, 32.6, 31.0, 29.9, 31.8, 27.4, 32.3, 34.6, 28.0, 25.1, 27.3, 29.9, 33.4, 31.6, 31.6, 45.9, 52.6, 47.3, 33.0, 21.9, 25.6, 25.9, 26.4, 23.9, 24.4, 23.3, 20.5, 21.3, 25.5, 20.8, 21.6]


beta2bis10_u = uarray(beta2bis10, 0.05)
betaFull_u = uarray(betaFull, 0.05)
beta18bis21_u = uarray(beta18bis21, 0.05)

zeroDegreeNaCl_u = uarray(zeroDegreeNaCl, np.array(zeroDegreeNaCl)*5/100)
oneEightyNaCl_u = uarray(oneEightyNaCl, np.array(oneEightyNaCl)*5/100)
NaCl18bis21_u = uarray(NaCl18bis21, np.array(NaCl18bis21)*5/100)

fig, ax = plt.subplots()



#ax.xaxis.set_major_locator(MultipleLocator(5))
#ax[1].xaxis.set_minor_locator(MultipleLocator(0.1))
#ax.grid(which='minor', color='#CCCCCC', linestyle=':')
#ax.grid(which='major', color='#CCCCCC', linestyle=':')

ax.set_xlabel("Beta")
ax.set_ylabel(r"Zählrate")

ax.errorbar(
        nominal_values(betaFull_u),
        nominal_values(zeroDegreeNaCl_u),
        label=r'NaCl Kristall 0° gedreht',
        color='purple',
        # linestyle='',
        marker='.',
        markersize=0.5,
        capsize=1.5,
        # elinewidth=1.2,
        xerr=std_devs(betaFull_u),
        yerr=std_devs(zeroDegreeNaCl_u)
)
ax.errorbar(
        nominal_values(beta2bis10_u),
        nominal_values(oneEightyNaCl_u),
        label=r'NaCl Kristall 180° gedreht',
        color='orange',
        # linestyle='',
        marker='.',
        markersize=0.5,
        capsize=1.5,
        # elinewidth=1.2,
        xerr=std_devs(beta2bis10_u),
        yerr=std_devs(oneEightyNaCl_u)
)
ax.errorbar(
        nominal_values(beta18bis21_u),
        nominal_values(NaCl18bis21_u),
        label=r'NaCl Messung mit $\Delta t = 4s$',
        color='red',
        # linestyle='',
        marker='.',
        markersize=0.5,
        capsize=1.5,
        # elinewidth=1.2,
        xerr=std_devs(beta18bis21_u),
        yerr=std_devs(NaCl18bis21_u)
)





ax.axvline(6.44, color='blue',linestyle='dashed',linewidth=0.8, label= r'$K_\beta$ für 0°')
#ax.text(6.35,1500,r'$K_\beta$ für 0°', rotation=90, color='purple')

ax.axvline(6.52, color='cyan',linestyle='dashed',linewidth=0.8, label = r'$K_\beta$ für 180°')
#ax.text(6.55,1250,r'$K_\beta$ für 180°', rotation=90, color='orange')

ax.axvline(7.25, color='green',linestyle='dashed',linewidth=0.8, label = r'$K_\alpha$ für 0°')
#ax.text(7.16,500,r'$K_\alpha$ für 0°', rotation=90, color='purple')

ax.axvline(7.33, color='magenta',linestyle='dashed',linewidth=0.8, label= r'$K_\alpha$ für 180°')

ax.axvline(12.9, color='blue',linestyle='dashed',linewidth=0.8)#, label= r'$K_\beta$ für 0°')
ax.axvline(14.54, color='green',linestyle='dashed',linewidth=0.8)#, label= r'$K_\beta$ für 0°')
ax.axvline(19.6, color='blue',linestyle='dashed',linewidth=0.8)#, label= r'$K_\beta$ für 0°')
ax.axvline(22.16, color='green',linestyle='dashed',linewidth=0.8)#, label= r'$K_\beta$ für 0°')

kBeta1O_0g=ufloat(6.44,0.11)
kBeta1O_180g=ufloat(6.52,0.11)
kAlpha1O_0g=ufloat(7.25,0.11)
kAlpha1O_180g=ufloat(7.33,0.11)
kBeta2O=ufloat(12.9,0.11)
kAlpha2O=ufloat(14.54,0.11)
kBeta3O=ufloat(19.6,0.11)
kAlpha3O=ufloat(22.16,0.11)


ax.text(7.8,1000, '1. Ordnung', rotation = 90, color='black')
ax.text(14.8,1000, '2. Ordnung', rotation = 90, color='black')
ax.text(22.4,1000, '3. Ordnung', rotation = 90, color='black')


#mittelwertBeta = (ufloat(6.44,0.11)+ufloat(6.52,0.11))/2
#mittelwertAlpha = (ufloat(7.25,0.11)+ufloat(7.33,0.11))/2
#mittelwertAlpha = ufloat(7.13,0.11)

mittelwertBeta = gf.weightedAverage(uarray([6.44,6.52],0.11))
mittelwertAlpha = gf.weightedAverage(uarray([7.25,7.33],0.11))
#print(mittelwertBeta)
#print(mittelwertAlpha)

def K_winkel(gem_winkel, Ordnung):
        a = 564.02*10**-12
        d = 282.01*10**-12#a/2
        return(2*d/Ordnung*unumpy.sin(gem_winkel*2*np.pi/360))

def E_winkel(gem_winkel, Ordnung):
    h = 4.1357 * 10**-15 # in eV
    c = 299792458
    return h*c/K_winkel(gem_winkel, Ordnung)



#print(K_winkel(mittelwertBeta,1)*10**12)
#print(K_winkel(mittelwertAlpha,1)*10**12)

def tabularWinkel():
    headers_temp = ["", r"$\beta$ 1.Ordnung ($\si{\degree}$)", r"$\alpha$ 1.Ordnung ($\si{\degree}$)", r"$\beta$ 2.Ordnung ($\si{\degree}$)", r"$\alpha$ 2.Ordnung ($\si{\degree}$)", r"$\beta$ 3.Ordnung ($\si{\degree}$)", r"$\alpha$ 3.Ordnung ($\si{\degree}$)"]
    headers = []
    for i in range(0, len(headers_temp)):
        headers.append("\\cellcolor[HTML]{C0C0C0}\\textbf{" + headers_temp[i] + "}")
    data = dict()
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Linie für $0\,\si{\degree}$" + "}"] = [gf.ufloatToTexStr(kBeta1O_0g),gf.ufloatToTexStr(kAlpha1O_0g),gf.ufloatToTexStr(kBeta2O),gf.ufloatToTexStr(kAlpha2O),gf.ufloatToTexStr(kBeta3O),gf.ufloatToTexStr(kAlpha3O)]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + r"Linie für $180\,\si{\degree}$" + "}"] = [gf.ufloatToTexStr(kBeta1O_180g),gf.ufloatToTexStr(kAlpha1O_180g),'nicht gemessen','nicht gemessen','nicht gemessen','nicht gemessen']
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "gewichteter Mittelwert" + "}"] = ["$6,48" + r" \pm " + '0,08' + "$","$7,29" + r" \pm " + '0,08' + "$",gf.ufloatToTexStr(kBeta2O),gf.ufloatToTexStr(kAlpha2O),gf.ufloatToTexStr(kBeta3O),gf.ufloatToTexStr(kAlpha3O)]

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
    print("\\caption{Bestimmte Werte für $K_\\alpha$ und $K_\\beta$}")
    print("\\label{tab:ErgebnisseKalphaE}")
    print("\\end{table}")

def tabularWelleEnergie():
    headers_temp = ["", r"$K_\beta$ ($\si{pm}$)", r"$K_\alpha$ ($\si{pm}$)", r"$E_\beta$ ($\si{keV}$)", r"$E_\alpha$ ($\si{keV}$)"]
    headers = []
    for i in range(0, len(headers_temp)):
        headers.append("\\cellcolor[HTML]{C0C0C0}\\textbf{" + headers_temp[i] + "}")
    data = dict()
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "1.Ordnung" + "}"] = [gf.ufloatToTexStr(K_winkel(mittelwertBeta,1)*10**12),gf.ufloatToTexStr(K_winkel(mittelwertAlpha,1)*10**12),gf.ufloatToTexStr(E_winkel(mittelwertBeta,1)/1000),gf.ufloatToTexStr(E_winkel(mittelwertAlpha,1)/1000)]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "2.Ordnung" + "}"] = [gf.ufloatToTexStr(K_winkel(kBeta2O,2)*10**12),gf.ufloatToTexStr(K_winkel(kAlpha2O,2)*10**12),gf.ufloatToTexStr(E_winkel(kBeta2O,2)/1000),gf.ufloatToTexStr(E_winkel(kAlpha2O,2)/1000)]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "3.Ordnung" + "}"] = [gf.ufloatToTexStr(K_winkel(kBeta3O,3)*10**12),gf.ufloatToTexStr(K_winkel(kAlpha3O,3)*10**12),gf.ufloatToTexStr(E_winkel(kBeta3O,3)/1000),gf.ufloatToTexStr(E_winkel(kAlpha3O,3)/1000)]
    data["\\cellcolor[HTML]{C0C0C0}\\textbf{" + "gewichteter Mittelwert" + "}"] = [gf.ufloatToTexStr(gf.weightedAverage(np.array([K_winkel(mittelwertBeta,1),K_winkel(kBeta2O,2),K_winkel(kBeta3O,3)]))*10**12),gf.ufloatToTexStr(gf.weightedAverage(np.array([K_winkel(mittelwertAlpha,1),K_winkel(kAlpha2O,2),K_winkel(kAlpha3O,3)]))*10**12),gf.ufloatToTexStr(gf.weightedAverage(np.array([E_winkel(mittelwertBeta,1),E_winkel(kBeta2O,2),E_winkel(kBeta3O,3)]))*10**-3),gf.ufloatToTexStr(gf.weightedAverage(np.array([E_winkel(mittelwertAlpha,1),E_winkel(kAlpha2O,2),E_winkel(kAlpha3O,3)]))/1000)]

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


tabularWinkel()



ax.set_xlim(2,25)
ax.legend()
plt.show()
