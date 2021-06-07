# Procesamiento digital de señales
# TP1 Punto 2(a)
# Blasi - Reyes - Sosa Lüchter
# ------------------------------------------------ #


def valor_medio(x):
    """
    Calcula el valor medio para una señal discreta x[n].
    :param x: señal discreta
    :return u: valor medio
    :type x: 1D ndarray

    """

    N = len(x)
    u = 1 / N * sum(x)
    return u


def desvio_medio(x):
    """
    Calcula el desvio medio para una señal discreta x[n].
    :param x: señal discreta
    :return d: desvio medio
    :type x: 1D ndarray
    """

    N = len(x)
    u = 1 / N * sum(x)
    d = 1 / N * sum(abs(x - u))
    return d


def desvio_estandar(x):
    """
    Calcula el desvio estandar para una señal discreta x[n].
    :param x: señal discreta
    :return sigma: desvio estandar
    :type x: 1D ndarray
    """

    from math import sqrt

    N = len(x)
    u = 1 / N * sum(x)
    arg = 1 / (N - 1) * sum((x - u) ** 2)
    sigma = sqrt(arg)
    return sigma


def rms(x):
    """
    Calcula el valor Root Mean Square (RMS) para una señal discreta x[n].
    :param x: señal discreta
    :return r: valor rms
    :type x: 1D ndarray
    """

    from math import sqrt

    N = len(x)
    r = sqrt(1 / N * sum(x ** 2))
    return r
