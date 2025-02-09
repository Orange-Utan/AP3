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


zeroDegreeNaCl = [6.0, 3.0, 2.0, 7.0, 5.0, 4.0, 4.0, 4.0, 4.0, 9.0, 3.0, 11.0, 19.0, 12.0, 13.0, 38.0, 129.0, 272.0, 435.0, 484.0, 584.0, 610.0, 653.0, 652.0, 696.0, 674.0, 655.0, 689.0, 625.0, 643.0, 612.0, 576.0, 520.0, 577.0, 566.0, 541.0, 485.0, 510.0, 482.0, 531.0, 508.0, 465.0, 509.0, 717.0, 980.0, 871.0, 676.0, 522.0, 459.0, 461.0, 614.0, 1140.0, 1888.0, 2002.0, 1137.0, 648.0, 469.0, 380.0, 344.0, 300.0, 309.0, 265.0, 275.0, 240.0, 233.0, 234.0, 217.0, 230.0, 238.0, 210.0, 206.0, 163.0, 191.0, 165.0, 159.0, 146.0, 133.0, 153.0, 136.0, 101.0, 122.0, 98.0, 114.0, 99.0, 107.0, 102.0, 91.0, 77.0, 90.0, 89.0, 83.0, 90.0, 102.0, 77.0, 95.0, 77.0, 88.0, 83.0, 91.0, 96.0, 69.0, 93.0, 68.0, 68.0, 85.0, 82.0, 89.0, 119.0, 172.0, 190.0, 173.0, 99.0, 82.0, 69.0, 72.0, 69.0, 73.0, 81.0, 59.0, 67.0, 65.0, 74.0, 72.0, 110.0, 313.0, 514.0, 437.0, 215.0, 110.0, 84.0, 55.0, 65.0, 65.0, 52.0, 64.0, 56.0, 58.0, 63.0, 42.0, 56.0, 46.0, 38.0, 55.0, 40.0, 44.0, 52.0, 54.0, 48.0, 38.0, 46.0, 44.0, 47.0, 38.0, 31.0, 32.0, 43.0, 35.0, 35.0, 38.0, 43.0, 33.0, 35.0, 38.0, 30.0, 28.0, 29.0, 32.0, 35.0, 25.0, 33.0, 28.0, 40.0, 22.0, 21.0, 24.0, 48.0, 54.0, 45.0, 37.0, 21.0, 32.0, 30.0, 22.0, 27.0, 22.0, 28.0, 16.0, 29.0, 22.0, 25.0, 19.0, 31.0, 23.0, 20.0, 25.0, 26.0, 25.0, 23.0, 23.0, 27.0, 51.0, 114.0, 126.0, 84.0, 56.0, 27.0, 21.0, 18.0, 14.0, 24.0, 16.0, 19.0, 23.0, 17.0, 17.0, 16.0, 21.0, 10.0, 13.0, 13.0, 16.0, 20.0, 12.0, 11.0, 16.0, 15.0, 18.0, 15.0, 14.0, 7.0, 10.0]
oneEightyNaCl = [2.0, 5.0, 3.0, 8.0, 7.0, 5.0, 7.0, 5.0, 7.0, 9.0, 6.0, 12.0, 16.0, 9.0, 24.0, 54.0, 105.0, 199.0, 328.0, 390.0, 479.0, 505.0, 515.0, 572.0, 582.0, 569.0, 535.0, 561.0, 516.0, 559.0, 487.0, 443.0, 441.0, 449.0, 499.0, 453.0, 431.0, 413.0, 414.0, 382.0, 412.0, 426.0, 388.0, 521.0, 714.0, 843.0, 713.0, 506.0, 399.0, 463.0, 507.0, 763.0, 1407.0, 1867.0, 1450.0, 797.0, 449.0, 364.0, 311.0, 272.0, 268.0, 261.0, 253.0, 253.0, 235.0, 250.0, 217.0, 179.0, 209.0, 187.0, 147.0, 157.0, 166.0, 137.0, 141.0, 123.0, 92.0, 118.0, 107.0, 106.0, 109.0]


beta2bis10_u = uarray(beta2bis10, 0.05)
betaFull_u = uarray(betaFull, 0.05)



fig, ax = plt.subplots(1,2)



#ax.xaxis.set_major_locator(MultipleLocator(5))
#ax[1].xaxis.set_minor_locator(MultipleLocator(0.1))
#ax.grid(which='minor', color='#CCCCCC', linestyle=':')
#ax.grid(which='major', color='#CCCCCC', linestyle=':')
for i in range(0,2):
        ax[i].set_xlabel("Beta")
        ax[i].set_ylabel(r"Zählrate")

        ax[i].errorbar(
                nominal_values(betaFull),
                zeroDegreeNaCl,
                label=r'NaCl Kristall 0° gedreht',
                color='purple',
                # linestyle='',
                marker='.',
                markersize=0.5,
                capsize=1.5,
                # elinewidth=1.2,
                xerr=std_devs(betaFull_u),
                # yerr=std_devs(tanAlpha1)
        )
        ax[i].errorbar(
                nominal_values(beta2bis10_u),
                oneEightyNaCl,
                label=r'NaCl Kristall 180° gedreht',
                color='orange',
                # linestyle='',
                marker='.',
                markersize=0.5,
                capsize=1.5,
                # elinewidth=1.2,
                xerr=std_devs(beta2bis10_u),
                # yerr=std_devs(tanAlpha1)
        )

        ax[i].legend()

ax[1].set_title('Vergrößert')
ax[1].set_xlim(6,8)
ax[0].set_xlim(2,11)

ax[1].axvline(6.44, color='purple',linestyle='dashed')
ax[1].text(6.35,1500,r'$K_\beta$ für 0°', rotation=90, color='purple')

ax[1].axvline(6.52, color='orange',linestyle='dashed')
ax[1].text(6.55,1250,r'$K_\beta$ für 180°', rotation=90, color='orange')

ax[1].axvline(7.25, color='purple',linestyle='dashed')
ax[1].text(7.16,500,r'$K_\alpha$ für 0°', rotation=90, color='purple')

ax[1].axvline(7.33, color='orange',linestyle='dashed')
ax[1].text(7.36,300,r'$K_\alpha$ für 180°', rotation=90, color='orange')

#mittelwertBeta = (ufloat(6.44,0.11)+ufloat(6.52,0.11))/2
#mittelwertAlpha = (ufloat(7.25,0.11)+ufloat(7.33,0.11))/2
#mittelwertAlpha = ufloat(7.13,0.11)

mittelwertBeta = gf.weightedAverage(uarray([6.44,6.52],0.11))
mittelwertAlpha = gf.weightedAverage(uarray([7.25,7.33],0.11))
print(mittelwertBeta)
print(mittelwertAlpha)

def K_winkel(gem_winkel, Ordnung):
        a = 564.02*10**-12
        d = 282.01*10**-12#a/2
        return(2*d/Ordnung*unumpy.sin(gem_winkel*2*np.pi/360))



#print(K_winkel(mittelwertBeta,1)*10**12)
#print(K_winkel(mittelwertAlpha,1)*10**12)

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
    print("\\end{table}[]")

tabularXY()

plt.show()
