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

gitterpos = ufloat(10,0.05)
gitterdick = ufloat(0.5,0.05)
schirmpos = uarray([50,70,90],0.05)
schirmdick = ufloat(1.6,0.05)

l=[1,2,3]
for i in range(3):
    l[i]= schirmpos[i]+0.5*schirmdick-(gitterpos-0.5*gitterdick)

#Unsicherheiten zeichnen 0,05mm  messen 0,05cm

l1_o_links = uarray([0.0, -2.36, -4.875, -7.3, -9.83, -12.525, -15.33],)
l1_o_rechts = uarray([0.0, 2.4, 4.81, 7.225, 9.73, 12.3, 15.8],)

l2_o_links = uarray([0.0, -3.55, -7.1, -10.825, -14.55, -18.55],)
l2_o_rechts = uarray([0.0, 3.5, 7.05, 10.6, 14.35, 18.15],)

l3_o_links = uarray([0.0, -4.7, -9.4, -14.15],)
l3_o_rechts = uarray([0.0, 4.7, 9.45, 14.3],)

l1_g_links = uarray([0.0, -2.275, -4.525, -6.85, -9.2, -11.8, -14.5],)
l1_g_rechts = uarray([0.0, 2.25, 4.45, 6.75, 9.175, 11.575, 14.0],)

l2_g_links = uarray([0.0, -3.35, -6.21, -10.2, -13.775, -17.6],)
l2_g_rechts = uarray([0.0, 3.3, 6.6, 10.25, 13.5, 17.1],)

l3_g_links = uarray([0.0, -4.45, -8.85, -13.3],)
l3_g_rechts = uarray([0.0, 4.45, 8.9, 13.5],)

l1_b_links= uarray([0.0, -1.8, -3.65, -5.475, -7.35, -9.35, -11.275],)
l1_b_links = uarray([0.0, 1.85, 3.675, 5.55, 7.25, 9.25, 11.175],)

l2_b_links = uarray([0.0, -2.7, -5.425, -8.11, -10.86, -13.825],)
l2_b_rechts = uarray([0.0, 2.675, 5.275, 8.0, 10.7, 13.5],)

l3_b_links= uarray([0.0, -3.5, -7.0, -10.8, -14.3],)
l3_b_rechts = uarray([0.0, 3.65, 7.25, 10.8, 14.4],)

