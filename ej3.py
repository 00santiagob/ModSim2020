import numpy as np
from random import random
import matplotlib.pyplot as plt
from timeit import timeit as timeit


def g(u):  # funcion a integrar en (0,1)
    return (1 - u**2)**(2.5)


def MonteCarlo(g, Nsim):
    # estimacion por el Monte Carlo con N simulaciones
    integral = 0
    for _ in range(Nsim):
        integral += g(random())
    return integral/Nsim


if __name__ == "__main__":  # Ejercicio
    for n in [1000, 10000, 100000]:
        print("\nCon {} simulaciones:".format(n))
        MediaI = MonteCarlo(g, n)
        print("Monte Carlo, I =", MediaI)
