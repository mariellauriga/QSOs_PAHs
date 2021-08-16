import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from scipy.interpolate import interp1d


a, a, a, a,z, D = loadtxt('/Users/mariela/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/pah_MM.dat', unpack=True)

f11p3, ef11p3, EW11p3, eEW11p3, logSFR_Shi14, elogSFR_Shi14, Lx = loadtxt('/Users/mariela/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/data_Shi14.dat', unpack=True)



f11p3 = f11p3*1.e-13
ef11p3 = ef11p3*1.e-13


Lsun = 3.826e+33 # erg s-1 cm-2

########IRS all QSOs

D[1:19] = D[1:19]*(1.e6)*(3.086e18) # cm
print D[-1]
L11p3 = arange(19)*0
errL11p3 = arange(19)*0
SFR11p3 = arange(19)*0
err_SFR11p3 = arange(19)*0


L11p3 = 4*pi*(D[1:19])**(2)*(f11p3[0:19])
errL11p3 =  4*pi*(D[1:19])**(2)*(ef11p3[0:19])

logSFR = -44.14 + 1.06*log10(L11p3)

SFR11p3 = 10**(logSFR)
err_SFR11p3 = sqrt((log(44.14)*L11p3**(1.06)*0.08/(10**(44.14)))**(2)+(errL11p3*1.06*L11p3**(0.06)/(10**(44.14)))**(2))


f10 = open('/Users/mariela/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/SFR_irs_Shi_etal.dat','w+')

print >>f10, '#L11p3(ergs-1)', ' ', 'eL11p3', ' ', 'SFR11p3 (Moyr-1)', ' ', 'eSFR11p3'
for i in range(0,len(L11p3)):
    print >>f10, L11p3[i], errL11p3[i], SFR11p3[i], err_SFR11p3[i]


f10.close()

L11p3_n, eL11p3_n, SFR11p3_n, eSFR11p3_n = loadtxt('/Users/mariela/Documents/QSOs-part2/QSOs-PAHs/IRS-decomp/spitzer_spectrum/SFR_irs_Shi_etal.dat', unpack=True)



SFR_DiamondRieke = (9.6e-9)*(L11p3_n)/(Lsun)


print '<SFR11p3_IRS=>', mean(SFR11p3_n),'STD=',std(SFR11p3_n)
print '<SFR11p3_IRS_Diamond_Rieke=>', mean(SFR_DiamondRieke),'SDT=',std(SFR_DiamondRieke)

SFR_Shi14 = 10**(logSFR_Shi14)

print '<SFR11p3_Shi14=>', mean(SFR_Shi14),'STD=',std(SFR_Shi14)
