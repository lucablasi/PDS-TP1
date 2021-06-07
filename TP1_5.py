# Procesamiento digital de señales
# TP1 Punto 5
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

from TP1_1a import gen_sig_p1
import numpy as np
from TP1_2a import desvio_estandar
import pandas as pd
import matplotlib.pyplot as plt

# Generar señal del punto 1
# ------------------------------------------------ #
[t, x] = gen_sig_p1()

# Generar 1, 10, 100, o 1000 señales de ruido, sumarlas a x para tener n señales x+ruido.
# Guardar en listas el promedio de las señales de ruido solas (para sacar sigma)
# y el promedio de las señales x+ruido
# ------------------------------------------------ #
noise_avg_list = []
x_avg_list = []
n_list = [1, 10, 100, 1000]
for n in n_list:
    noise_list = []     # Lista de señales de ruido individuales
    x_list = []         # Lista de señales x+ruido individuales
    for i in range(n):
        noise_i = np.random.normal(scale=3, size=len(x))    # Generar ruido
        x_i = x + noise_i                                   # Sumar ruido
        noise_list.append(noise_i)                          # Append ruido solo
        x_list.append(x_i)                                  # Append x+ruido

    # Tomar promedio de las n señales de ruido y las n señales x+ruido
    # Append a listas de promedios
    noise_avg = sum(noise_list) / len(noise_list)
    x_avg = sum(x_list) / len(x_list)
    noise_avg_list.append(noise_avg)
    x_avg_list.append(x_avg)

# Calcular y guardar en listas el std y S/N para cada caso de N
# ------------------------------------------------ #
std_list = [desvio_estandar(i) for i in noise_avg_list]
sn_list = [(max(x) - min(x)) / i for i in std_list]

# Organizar en un hermoso dataframe
df_data = list(zip(n_list, std_list, sn_list))
df = pd.DataFrame(df_data, columns=['N', 'std', 'S/N'])
print(df.round(3))

# Gráfico
# ------------------------------------------------ #
fig, ax = plt.subplots(nrows=4, ncols=1)

# Plot data
for i in range(4):
    ax[i].plot(t, x_avg_list[i])
    ax[i].set_title('N = ' + str(n_list[i]))

# Detalles
fig.suptitle('TP1 Punto 5', weight='bold', ha='left', x=0.05)
ax[-1].set_xlabel('t [s]')
plt.tight_layout()

# Plot!
plt.show()
