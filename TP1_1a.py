def gen_sig_p1():

    import numpy as np

    # Definición variable independiente 't'
    T = 1  # Duración [s]
    fs = 44.1 * 10 ** 3  # Sample rate
    t = np.arange(0, T, 1 / fs)

    # Definición señal x1(t)
    x1 = np.array([2 for i in t])

    # Definición señal x2(t)
    f2 = 10 * 10 ** 3
    u2 = 0.2
    sigma2 = 0.05
    w2 = 2 * np.pi * f2
    sub_arg = -((t - u2) ** 2) / (2 * sigma2 ** 2)
    x2 = np.cos(w2 * t) * np.e ** sub_arg

    # Definición señal x3(t)
    f3 = 10.1 * 10 ** 3
    u3 = 0.7
    sigma3 = 0.07
    w3 = 2 * np.pi * f3
    sub_arg = -((t - u3) ** 2) / (2 * sigma3 ** 2)
    x3 = np.sin(w3 * t) * np.e ** sub_arg

    # Definición señal x(t)
    x = x1 + x2 + x3
    return [t, x]
