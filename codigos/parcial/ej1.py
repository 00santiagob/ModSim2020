import numpy as np
from random import random
import matplotlib.pyplot as plt
from timeit import timeit as timeit
from scipy.stats import norm

def K_S(datos, mu, sigma):
    'Estadıstico de Kolmogorov Smirnov'
    n = len(datos)
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j+1)/n-norm.cdf((x-mu)/sigma), norm.cdf((x-mu)/sigma)-j/n)
        return d


def ej1_d():
    d_KS = 0.1017
    mu = 4.347  # media
    sigma = 1.4558  # desvio estandar
    pvalor = 0
    n = 20
    Nsim = 10000
    for _ in range(Nsim):
        datos = np.random.normal(mu, sigma, n) #creando muestra de datos
        datos.sort()
        dj = 0
        for _ in range(n):
            dj = K_S(datos, mu, sigma)
        if dj >= d_KS:
            pvalor += 1
    print(pvalor/Nsim)


def ej1_c():
    d_KS =  0.1017  #estadıstico
    pvalor = 0
    n = 20
    Nsim = 10000
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_j= 0
        for j in range(n):
            u_j = uniformes[j]
            d_j = max(d_j, (j+1)/n-u_j, u_j-j/n)
        if d_j >= d_KS:
            pvalor += 1
    print(pvalor/Nsim)


if __name__ == "__main__":
    # ej1_c()
    ej1_d()
