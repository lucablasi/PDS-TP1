# Procesamiento digital de señales
# TP1 Punto 4
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

from TP1_1a import gen_sig_p1
import numpy as np
import matplotlib.pyplot as plt

# Generar señales
# ------------------------------------------------ #
[t, x] = gen_sig_p1()

# Aplicar ruido
# ------------------------------------------------ #
# Generar ruido
noise01 = np.random.normal(scale=0.1, size=len(x))
noise1 = np.random.normal(scale=1, size=len(x))
noise3 = np.random.normal(scale=3, size=len(x))

# Sumar ruido
x01 = x + noise01
x1 = x + noise1
x3 = x + noise3

# Normalizar
x01 = x01 / max(x01)
x1 = x1 / max(x1)
x3 = x3 / max(x3)

# Graficar
# ------------------------------------------------ #
fig, ax = plt.subplots(nrows=3, ncols=1)

# Plot data
ax[0].plot(t, x01)
ax[1].plot(t, x1)
ax[2].plot(t, x3)

# Título para cada subplot
ax[0].set_title('x01(t)')
ax[1].set_title('x1(t)')
ax[2].set_title('x3(t)')

# Detalles
fig.suptitle('TP1 Punto 4', weight='bold', ha='left', x=0.05)
ax[2].set_xlabel('t [s]')
plt.tight_layout()

# Calcular relación señal/ruido
# ------------------------------------------------ #
# Amplitud
a = max(x) - min(x)

# S/N ratio
sn01 = a / 0.1
sn1 = a / 1
sn3 = a / 3

# Print
print('sn01: ' + str(sn01))
print('sn1: ' + str(sn1))
print('sn3: ' + str(sn3))

# Graph
plt.show()
