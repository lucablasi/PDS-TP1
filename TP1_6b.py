# Procesamiento digital de señales
# TP1 Punto 6(b)
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #

from TP1_6a import mediamovild as mmd
from TP1_6a import mediamovilr as mmr
from TP1_1a import gen_sig_p1
import time

# Importar función del punto 1
[t, x] = gen_sig_p1()

# Tamaño de ventana
M = 100

# Para calcular el tiempo de ejecución se corre la función diez veces y se divide el tiempo calculado por 10.
# Esto se hace para minimizar diferencias de ejecución entre diferentes instancias y obtener un promedio
# mas representativo.

print('Calculando implementación directa...')
start = time.time()
for i in range(10):
    yd = mmd(x, M)
end = time.time()
tiempo_d = (end - start)/10
print('Done!')
print()

print('Calculando implementación recursiva...')
start = time.time()
for i in range(10):
    yr = mmr(x, M)
end = time.time()
tiempo_r = (end - start)/10
print('Done!')
print()

print('Tiempo de ejecución:')
print(' Implementación directa: ' + str(round(tiempo_d, 3)) + ' s')
print(' Implementación recursiva: ' + str(round(tiempo_r, 3)) + ' s')
print()
prcnt = (tiempo_d/tiempo_r)*100
print(' Cociente porcentual: ' + str(int(prcnt)) + '%')
print()
if prcnt > 1000:
    print(' La implementación recursiva fue altamente exitosa!!!')
else:
    print('):')
