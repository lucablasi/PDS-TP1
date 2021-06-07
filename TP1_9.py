# Procesamiento digital de señales
# TP1 Punto 1
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

import numpy as np
import matplotlib.pyplot as plt
import librosa as lb
from scipy.io import wavfile
from conv_circular import circular_convolve

x, srx = lb.load('Midi69.wav', sr = None)

h, srh = lb.load('Resp_Imp.wav', sr = None)

# =============================================================================
# Convolucion Lineal
# =============================================================================

x_lineal = x[:len(h)]

y_lineal = np.convolve(x,h)

t_lineal = len(y_lineal)/srx

t_lineal = np.linspace(0, t_lineal, len(y_lineal))

# =============================================================================
# Convolucion Circular
# =============================================================================

x_circ = x[:len(h)]

y_circ = circular_convolve(x_circ,h,len(h)) 

t_circ = len(y_circ)/srx

t_circ = np.linspace(0, t_circ, len(y_circ))


# =============================================================================
# Convolucion Circular = Convolucion Lineal
# =============================================================================

x_cl = x[:len(h)]

# len(x) y len(h) deben ser >= a N  para que conv_lineal = conv_circular

N = len(x) + len(h) - 1

zeros = np.zeros(N-len(x)) #Cantidad de ceros que debo agregar para llegar a N

x_cl = np.concatenate((x, zeros))

h_cl = np.concatenate((h, zeros))

y_cl = circular_convolve(x_cl,h_cl,N)

t_cl = len(y_cl)/srx

t_cl = np.linspace(0, t_cl, len(y_cl))

fig, ax = plt.subplots(nrows=3, ncols=1)

ax[0].plot(t_lineal, y_lineal)
ax[1].plot(t_circ, y_circ)
ax[2].plot(t_cl, y_cl)

ax[0].set_title('Convolución Lineal')
ax[1].set_title('Convolución Circular')
ax[2].set_title('Convolución Circular = Convolución Lineal')

fig.suptitle('TP1 Punto 9', weight='bold', ha='left', x=0.05)
ax[2].set_xlabel('t [s]')

plt.tight_layout()

plt.show()


#Exportar .wav
wavfile.write('convolucion_lineal.wav',srx, y_lineal)
wavfile.write('convolucion_circular.wav',srx, y_circ)
wavfile.write('convolucion_lineal_circular.wav',srx, y_cl)
