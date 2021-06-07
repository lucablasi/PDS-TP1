# Procesamiento digital de señales
# TP1 Punto 2(b)
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

import numpy as np
from TP1_2a import valor_medio, desvio_medio, desvio_estandar, rms
import pandas as pd

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

# Calcular e imprimir parámetros para cada señal
# ------------------------------------------------ #
data_list = []
x_list = [x1, x2, x3, x4]
for xi in x_list:
    # Calcular parámetros
    u = valor_medio(xi)
    d = desvio_medio(xi)
    std = desvio_estandar(xi)
    r = rms(xi)

    # Crear lista de param para cada señal, append a data_list
    sub_list = [u, d, std, r]
    data_list.append(sub_list)

# Definir dataframe
idx = ['Señal 1', 'Señal 2', 'Señal 3', 'Señal 4']
cols = ['u', 'd', 'std', 'RMS']
df = pd.DataFrame(data_list, idx, cols)
print(df.round(3))
