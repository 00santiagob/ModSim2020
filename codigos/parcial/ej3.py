import numpy as np
from random import random
import matplotlib.pyplot as plt
from timeit import timeit as timeit


def g(u):  # funcion a integrar en (0,1)
    return (1 - u**2)**(2.5)


def MonteCarlo(g, Nsim):
    # estimacion por el Monte Carlo con N simulaciones
    # se modifico para que almacene los g(u)
    integral = 0
    gu = []
    for i in range(Nsim):
        gu.append(g(random()))
        integral += gu[i]
    return integral/Nsim, gu


def DesvioEstandar_X(N, Media, Xi):
    S = 0
    for i in range(N):
        S += (Xi[i] - Media)**2
    return np.sqrt(S/(N-1))


if __name__ == "__main__":  # Ejercicio
    for n in [1000, 10000, 100000]:
        print("\nCon {} simulaciones:".format(n))
        MediaI, gu = MonteCarlo(g, n)
        S = DesvioEstandar_X(n, MediaI, gu)
        print("Monte Carlo, I =", MediaI)
        print("Desviacion Estandar S =", S)
