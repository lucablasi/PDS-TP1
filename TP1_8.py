# Procesamiento digital de señales
# TP1 Punto 8
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

from TP1_6a import mediamovilr
import numpy as np
import matplotlib.pyplot as plt


def blackman(x, M):
    n = np.arange(M+1)

    a0 = 0.42
    a1 = 0.5
    a2 = 0.08

    v = a0 - a1 * np.cos((2 * np.pi * n) / (M - 1)) + a2 * np.cos((4 * np.pi * n) / (M - 1))
    y = np.convolve(x, v)
    y = y / (M+1)

    return y


# Crear señal ruido
lenght = 500
m = int(lenght * 0.01)
x1 = np.random.normal(scale=1, size=lenght)

# Aplicar filtros
yr = mediamovilr(x1, m)
yb = blackman(x1, m)

# Normalizar
x1 = x1 / max(abs(x1))
yr = yr / max(abs(yr))
yb = yb / max(abs(yb))

# Graficar
fig, ax = plt.subplots(nrows=3, ncols=1)

ax[0].plot(x1)
ax[1].plot(yr)
ax[2].plot(yb)

ax[0].set_title('Señal original')
ax[1].set_title('Implementación recursiva')
ax[2].set_title('Ventana de Blackman')

fig.suptitle('TP1 Punto 8', weight='bold', ha='left', x=0.05)
plt.tight_layout()

plt.show()
