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

#Ungenau: Messkala 0,5mm,Scharfstellen rechts 1mm,Scharfstellen links 3mm


gegenstand = 19.0


linksabs_b = [31.4, 31.2, 30.9, 31.0, 30.9]
rechtsabs_b = [72.8, 72.6, 72.9, 73.05, 73.0]
schirm_b = [85.0, 85.0, 85.0, 85.0, 85.0]

linksabs_g = [27.5, 28.0, 27.8, 27.7, 28.0]
rechtsabs_g = [58.0, 57.9, 58.1, 57.95, 57.9]
schirm_g = [67.0, 67.0, 67.0, 67.0, 67.0]