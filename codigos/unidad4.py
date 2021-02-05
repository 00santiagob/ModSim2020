# Modelos y Simulacion (2020)
# Unidad 4
# Autor: @00santiagob (GitHub)

from random import random
from numpy import exp, cos
import numpy as np

#########################
# Metodo de Monte Carlo #
#########################

# Integracion sobre un intervalo (0, 1)

def g_01(u): # funcion a integrar
    return (1 - u ** 2) ** (1.5)

def monteCarlo_01(g, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += g(random())
    return Integral / Nsim

def ej_MonteCarlo1():
    for Nsim in [1000, 10000, 100000, 1000000]:
        print("Nsim=", Nsim, ":", monteCarlo_01(g_01, Nsim))

# Integracion sobre un intervalo (a, b)

def g_ab(x): # funcion a integrar
    return exp(x ** 2 + x)

def monteCarlo_ab(g, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += g(a + (b-a) * random())
    return Integral * (b-a) / Nsim

def ej_MonteCarlo2():
    for Nsim in [1000, 10000, 100000, 1000000, 10000000]:
        print("Nsim=", Nsim, ":", monteCarlo_ab(g_ab, -1, 1, Nsim))

# Integracion sobre un intervalo (0, inf)

def g_0Inf(x): # funcion a integrar
    return cos(x) * exp(-x)

def monteCarlo_0Inf(g, Nsim):
    Integral = 0
    for _ in range(Nsim):
        u = random()
        Integral += g((1/u) - 1) / u**2
    return Integral / Nsim

def ej_MonteCarlo3():
    for Nsim in [1000, 10000, 100000, 1000000]:
        print("Nsim=", Nsim, ":", monteCarlo_0Inf(g_0Inf, Nsim))

# Estimacion de PI

def valorPI(Nsim):
    enCirculo = 0
    for _ in range(Nsim):
        u = 2 * random() - 1
        v = 2 * random() - 1
        if u ** 2 + v ** 2 <= 1:
            enCirculo += 1
    return 4 * enCirculo / Nsim

def ej_PI():
    for Nsim in [1000, 10000, 100000, 1000000, 10000000]:
        print("Nsim=", Nsim, ":", valorPI(Nsim))

if __name__ == "__main__":
    # ej_MonteCarlo1()
    # ej_MonteCarlo2()
    # ej_MonteCarlo3()
    ej_PI()