# Procesamiento digital de señales
# TP1 Punto 6(a)
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #


def mediamovild(x, M):
    """
    Filtro de media movil. Implementación directa.
    :param x: Señal
    :param M: Tamaño de la ventana
    :return:
    """

    import numpy as np

    xN = len(x)
    y = np.zeros(xN - M + 1)
    yN = len(y)

    for i in range(yN):
        y[i] = sum(x[i: i+M]) / M
    return y


def mediamovilr(x, M):
    """
    Filtro de media movil. Implementación recursiva.
    :param x: Señal
    :param M: Tamaño de la ventana
    :return:
    """
    import numpy as np

    xN = len(x)
    y = np.zeros(xN - M + 1)
    yN = len(y)

    for i in range(M):
        y[0] += x[i]

    for i in range(1, yN):
        y[i] = y[i - 1] - x[i - 1] + x[i + M - 1]

    y = y / M
    return y
