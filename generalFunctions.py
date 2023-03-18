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


test = uarray([1,2,3],[0.1,0.2,0.3])

def weightedAverage(werte):
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

