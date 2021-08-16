import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from matplotlib.patches import Ellipse, Polygon
import math
import scipy.optimize as optimization
from scipy.interpolate import interp1d
from scipy.stats import *
from scipy.special import erf
from scipy import stats

dl=(359.0,367.6,409.5,395.0,263.5,460.3)
Lx=(5.8e43,5.0e43,2.5e43, 1.3e44, 7.1e43, 2.9e44)
#Names = (PG1440+356,PG1211+143,PG1411+442, PG1426+015, IZw1,PG0804+761)
def Lx2Lbol(Lx): 
    k = (0.057254*math.pow(np.log10(Lx)-40.,4.)) - (0.4328*math.pow(np.log10(Lx)-40.,3.)) + (1.6725*math.pow(np.log10(Lx)-40.,2.)) - (2.9138*(np.log10(Lx)-40.)) + 8.5206 
    return k, k*Lx


f1 = open('/Users/administrador/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/Lbol_all_g3.dat','w+')
for x in Lx:
 kPAH, Lbol_PAH = (Lx2Lbol(x))
 print >>f1, kPAH, Lbol_PAH
f1.close()

k_p, Lbol_p = loadtxt('/Users/administrador/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/Lbol_all_g3.dat', unpack=True) 
epsilon=0.1 # typical value for the mass-energy conversion efficiency in the local universe (Marconi et al. 2004)
#Usando la luminosidad corregida por absorbcion (Esquej et al. 2014) de MRK509.
#Maccret_mrk509 = 0.15*(epsilon/0.1)*(10**(45.4)/10**(45))
###########################################################

Maccret = 0.15*(epsilon/0.1)*(Lbol_p/10**(45))
e_Maccret = 0.1*Maccret


print 'Maccret=',mean(Maccret),'+/-','',std(Maccret),'Mo Yr-1'

