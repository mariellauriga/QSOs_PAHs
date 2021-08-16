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


SFR_irs, eSFR_irs, SFR_inner, eSFR_inner  = loadtxt('SFR_inner_irs.dat', unpack=True)
logeSFR_irs = eSFR_irs/(SFR_irs*log(10))
logeSFR_inner = eSFR_inner/(SFR_inner*log(10))

plt.figure()
plt.errorbar(log10(SFR_inner), log10(SFR_irs), xerr=logeSFR_inner, yerr=logeSFR_irs, fmt='*', markersize=14, color='blue')

plt.errorbar(log10(3.), log10(6.), xerr=1./(3.*log(10)), yerr=2./(6.*log(10)), fmt='s', markersize=12, color='blue') #PG1440+356


plt.plot(log10(0.2), log10(0.2),'*', markersize=14, color='blue')
arrow(log10(0.2), log10(0.2),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG1501+106
arrow(log10(0.2), log10(0.2),0, -0.1,head_width=0.1, head_length=0.1,color='blue')

plt.plot(log10(0.4), log10(0.5),'s', markersize=12, color='blue')
arrow(log10(0.4), log10(0.5),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG0804+349
arrow(log10(0.4), log10(0.5),0, -0.1,head_width=0.1, head_length=0.1,color='blue')

plt.plot(log10(1.5), log10(1.2),'s', markersize=12, color='blue')
arrow(log10(1.5), log10(1.2),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG1211+143
arrow(log10(1.5), log10(1.2),0, -0.1,head_width=0.1, head_length=0.1,color='blue')


arrow(log10(1.9), log10(1.7),0, -0.1,head_width=0.1, head_length=0.1,color='blue')#PG1426+015
plt.errorbar(log10(1.9), log10(1.7), xerr=0.6/(1.9*log(10)), fmt='s', markersize=12, color='blue')

plt.plot(log10(0.9), log10(1.5),'s', markersize=12, color='blue')
arrow(log10(0.9), log10(1.5),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG1411+442
arrow(log10(0.9), log10(1.5),0, -0.1,head_width=0.1, head_length=0.1,color='blue')

arrow(log10(1.), log10(3.),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG0050+124
plt.errorbar(log10(1.), log10(3.), yerr=1./(3.*log(10)), fmt='s', markersize=12, color='blue')

plt.plot(log10(1.2), log10(1.1),'s', markersize=12, color='blue')
arrow(log10(1.2), log10(1.1),-0.07,0,head_width=0.1, head_length=0.07,color='blue') #PG0804+761
arrow(log10(1.2), log10(1.1),0, -0.1,head_width=0.1, head_length=0.1,color='blue')

arrow(log10(0.3), log10(0.7),-0.07,0,head_width=0.1, head_length=0.07,color='red') #Group 1
plt.errorbar(log10(0.3), log10(0.7), yerr=0.2/(0.7*log(10)), fmt='*', markersize=22, color='red')
text(log10(0.2), log10(0.9),'Group 1', fontsize='16')

plt.errorbar(log10(1.6), log10(1.6), yerr=0.5/(1.6*log(10)), xerr=0.5/(1.6*log(10)), fmt='s', markersize=16, color='red') #Group 2
text(log10(1.3), log10(2.1),'Group 2', fontsize='16')


plt.xlabel("logSFR$_{inner}$ (M$_{\odot}$ yr$^{-1}$), this work",fontsize=18)
plt.ylabel("logSFR$_{IRS}$ (M$_{\odot}$ yr$^{-1}$), this work",fontsize=18)


tick_params(axis='x', labelsize=20)
tick_params(axis='y', labelsize=20)

plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)

y0=(-1.5,2.)
x0=(-1.5,2.)

plt.plot(x0,y0,'k--')


plt.show()
