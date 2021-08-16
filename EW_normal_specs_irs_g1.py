import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from scipy.interpolate import interp1d

#Reading the spectra
import normal_specs_irs_all_by_scale_new as nspec

#Making the continumm

plt.plot(nspec.xspit_new, nspec.yspit_g1, color='brown', label='Spitzer/IRS')

print nspec.xspit_new[0], nspec.xspit_new[-1]
f1 = interp1d(nspec.xspit_new, nspec.yspit_g1)
ferr = interp1d(nspec.xspit_new, nspec.eyspit_g1)

#Rango para calcular el continuo
#Rango para restar el espectro del continuo

l4 = arange(7.64,13.0,0.01,dtype=float)
fnuc_all = f1(l4)

l3 = arange(10.96,11.59,0.01,dtype=float)
l1 = arange(4)
l2 = arange(4)

fnuc = f1(l3)
fnuc = fnuc/1000.  #Jy
fnuc = fnuc*1.e-23  # erg s-1 cm-2 Hz-1

efnuc = ferr(l3) # mJy
efnuc = efnuc/1000.  #Jy
efnuc = efnuc*1.e-23  # erg s-1 cm-2 Hz-1


f10 = open('band1.dat', 'w+')
f20 = open('band2.dat', 'w+')
for i in range(0,100):
###Imprime las bandas###
    l1 = np.random.uniform(10.70, 10.95, 100)
    fc1 = f1(l1)
    efc1 = ferr(l1)
    pfc1 = mean(fc1)
    epfc1 = mean(efc1)
    pl1 = mean(l1)    
    print >>f10, pl1, pfc1, pfc1+epfc1, pfc1-epfc1

    l2 = np.random.uniform(11.60, 11.80, 100)
    fc2 = f1(l2)
    efc2 = ferr(l2)
    pfc2 = mean(fc2)
    epfc2 = mean(efc2)
    pl2 = mean(l2)
    print >>f20, pl2, pfc2, pfc2+epfc2, pfc2-epfc2
##############################
f10.close()
f20.close()

xpl1, ypfc1, up_pfc1, low_pfc1 = loadtxt('band1.dat', unpack=True)
xpl2, ypfc2, up_pfc2, low_pfc2 = loadtxt('band2.dat', unpack=True)

plt.figure()

f100 = open('temp_n.dat', 'w+')
for i in range(0,100):
    s1 = np.random.uniform(low_pfc1[i], up_pfc1[i], 100)
    s1_m = mean(s1)

    s2 = np.random.uniform(low_pfc2[i], up_pfc2[i], 100)
    s2_m = mean(s2)
    
    l1_2 = (xpl1[i],xpl2[i])
    f1_2 = (s1_m, s2_m)
    
    f2 = interp1d(l1_2, f1_2)
    fcont = f2(l3)
    fcont = fcont/1000.  #Jy
    fcont = fcont*1.e-23  # erg s-1 cm-2 Hz-1
    res = fnuc-fcont
    f200 = open('temp2n.dat', 'w+')
    for j in range(0,len(l3)):
          if res[j] > 0:
            print >>f200, l3[j], res[j], efnuc[j]
    f200.close()        
    nl3,res2, eres2 = genfromtxt('temp2n.dat', dtype='float',unpack='True')
    nurange =  ((7.04832015036e+26)*(nl3[-1]-nl3[0]))/(3.e14) # Hz
    h3=nurange/(2*len(nl3))# En Hz
    h3_1 = (nl3[-1]-nl3[0])/(2*len(nl3)) # En microns    
    few = h3*(sum(2*res2[1:-1])+res2[0]+res2[-1]) #erg s-1 cm-2
    efew = h3*(sum(2*eres2[1:-1])+eres2[0]+eres2[-1]) #erg s-1 cm-2
    few_1 = h3_1*(sum(2*res2[1:-1])+res2[0]+res2[-1]) #erg s-1 cm-2 Hz-1 um 
    ew = few_1/fcont[37] # um
    print l3[37]
    print >>f100, few, efew, ew
    plt.plot(l3,fnuc/1.e-26, color='blue')
    plt.plot(l3,fcont/1.e-26, color='red')
    plt.plot(nspec.xspit_new, nspec.yspit_g1, color='blue')
    plt.fill_between(nspec.xspit_new, nspec.yspit_g1,(nspec.yspit_g1+nspec.eyspit_g1), color='LightBlue')
    plt.fill_between(nspec.xspit_new, nspec.yspit_g1,(nspec.yspit_g1-nspec.eyspit_g1), color='LightBlue')
f100.close()

############Calculo del EW##################
all_few, all_efew, all_ew = loadtxt('temp_n.dat', unpack='True')

m_few = mean(all_few)
m_ew = mean(all_ew)

std_few = std(all_few)
std_ew = std(all_ew)

print 'PAH11.3um (IRS):'
print 'Flux=', m_few,'+/-', std_few, 'units= erg s-1 cm-2'
print 'EW=', m_ew, '+/-', std_ew, 'units=microns' 

##############################

xpah1 = (11.3,11.3)
ypah1 = (80,220)

plt.plot(xpah1, ypah1, 'k--')

xSIV1 = (10.5,10.5)
ySIV1 = (80,220)

plt.plot(xSIV1, ySIV1, 'k--')

#plt.ylim(83,205)

text(8.,120,'Group 1', fontsize=18)


plt.fill([10.70,10.95,10.95,10.70],[0,0,300,300], color='pink',fill=False, hatch='\\',linewidth=3)
plt.fill([11.60,11.80,11.80,11.60],[0,0,300,300], color='pink',fill=False, hatch='\\', linewidth=3)


tick_params(axis='x', labelsize=18)
tick_params(axis='y', labelsize=18)
plt.ylabel(r" $f_{\nu}$ (mJy)",fontsize=22)
plt.xlabel("Rest-frame wavelength ($\mu$m)",fontsize=22)


plt.show()
