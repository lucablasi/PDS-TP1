# Procesamiento digital de señales
# TP1 Punto 7
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

from TP1_6a import mediamovilr
import numpy as np
import matplotlib.pyplot as plt


def mediamovilconv(x, M):

    h = np.ones(M+1)
    y = np.convolve(x, h, mode='valid')
    y = y / (M+1)

    return y


# Crear señal ruido
lenght = 500
m = int(lenght * 0.01)
x1 = np.random.normal(scale=1, size=lenght)
x1 = x1

# Aplicar filtros
yr = mediamovilr(x1, m)
yc = mediamovilconv(x1, m)

# Normalizar
x1 = x1 / max(abs(x1))
yr = yr / max(abs(yr))
yc = yc / max(abs(yc))

# Graficar
fig, ax = plt.subplots(nrows=3, ncols=1)

ax[0].plot(x1)
ax[1].plot(yr)
ax[2].plot(yc)

ax[0].set_title('Señal original')
ax[1].set_title('Implementación recursiva')
ax[2].set_title('Implementación por convolución')

fig.suptitle('TP1 Punto 7', weight='bold', ha='left', x=0.05)
plt.tight_layout()

plt.show()
