import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as scipy
import matplotlib.lines as mlines
import itertools
from scipy.interpolate import interp1d

import NOISE_B1_g1 as ns_b1
import NOISE_B2_g1 as ns_b2
import NOISE_B3_g1 as ns_b3
import SIGNAL_g1   as sg

#noise = (ns_b1.signal, ns_b1.signal, ns_b3.signal)
#enoise_v = (ns_b1.esignal, ns_b1.esignal, ns_b3.esignal)
noise = (ns_b1.signal, ns_b1.signal)
enoise_v = (ns_b1.esignal, ns_b1.esignal)
noise_mean = mean(noise)
enoise = mean(enoise_v)
SNR1 = sg.signal/noise_mean
SNR2 = sg.signal/enoise
print 'Noise=', noise_mean, '+/-', np.std(noise), '+/-', enoise
print 'Signal=', sg.signal, '+/-', sg.esignal
print 'SNR_G1-1 =', SNR1
print 'SNR_G1-2 =', SNR2
