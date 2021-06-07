# Procesamiento digital de señales
# TP1 Punto 3
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

import numpy as np
from TP1_2a import desvio_estandar
import pandas as pd

N = [5, 10, 100, 1000, 10000, 100000]

data_list = []

for i in N:
    x = np.random.normal(scale=1, size=i)
    std = desvio_estandar(x)
    dif = abs(1 - std) * 100

    # Crear lista de param para cada señal, append a data_list
    sub_list = [i, std, dif]
    data_list.append(sub_list)

# Definir dataframe
idx = ['Señal 1', 'Señal 2', 'Señal 3', 'Señal 4', 'Señal 5', 'Señal 6']
cols = ['N', 'std', 'Diferencia %']
df = pd.DataFrame(data_list, idx, cols)
print(df.round(3))
