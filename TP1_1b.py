# Procesamiento digital de señales
# TP1 Punto 1
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

import numpy as np
import matplotlib.pyplot as plt

# Generar señales
# ------------------------------------------------ #
# Definición variable independiente 't'
T = 1               # Duración [s]
fs = 44.1*10**3     # Sample rate
t = np.arange(0, T, 1/fs)

# Definición señal x1(t)
x1 = np.array([2 for i in t])

# Definición señal x2(t)
f2 = 10*10**3
u2 = 0.2
sigma2 = 0.05
w2 = 2 * np.pi * f2
sub_arg = -((t - u2)**2)/(2 * sigma2**2)
x2 = np.cos(w2 * t) * np.e ** sub_arg

# Definición señal x3(t)
f3 = 10.1*10**3
u3 = 0.7
sigma3 = 0.07
w3 = 2 * np.pi * f3
sub_arg = -((t - u3)**2)/(2 * sigma3**2)
x3 = np.sin(w3 * t) * np.e ** sub_arg

# Definición señal x(t)
x4 = x1 + x2 + x3

# Gráfico
# ------------------------------------------------ #
# Crear figura que contiene a 'ax'
# ax es un array que contiene 4 elementos, uno para cada subplot individual
fig, ax = plt.subplots(nrows=4, ncols=1)

# Plot data
ax[0].plot(t, x1)
ax[1].plot(t, x2)
ax[2].plot(t, x3)
ax[3].plot(t, x4)

# Título para cada subplot
ax[0].set_title('x1(t)')
ax[1].set_title('x2(t)')
ax[2].set_title('x3(t)')
ax[3].set_title('x(t)=x1(t)+x2(t)+x3(t)')

# Título de la figura, ajustes, xlabel en último gráfico
fig.suptitle('TP1 Punto 1', weight='bold', ha='left', x=0.05)
ax[0].set_ylim(top=3, bottom=1)
ax[3].set_xlabel('t [s]')

# Acomoda subplots para que no se sobrelapen
plt.tight_layout()

plt.show()
