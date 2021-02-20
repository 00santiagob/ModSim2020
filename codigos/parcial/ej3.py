import numpy as np
from numpy import sqrt
from random import random


def g(u):  # funcion a integrar en (0,1)
    return (1 - u**2)**(2.5)


def MonteCarlo(g, Nsim):
    # estimacion por el Monte Carlo con N simulaciones
    integral = 0
    for _ in range(Nsim):
        integral += g(random())
    return integral/Nsim

def monteCarlo_intervalo_sinL(g, Nsim): # z_alfa_2 = z(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    MonteCarlo_media = g(random()) # g(U1)
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n <= Nsim:
        n += 1
        Ui = g(random()) # g(Ui)
        Media_Ant = MonteCarlo_media
        MonteCarlo_media = Media_Ant + (Ui - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (MonteCarlo_media - Media_Ant)**2
    return MonteCarlo_media, Scuad

def monteCarlo_intervalo_sinN(z_alfa_2, g, L): # z_alfa_2 = z(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    MonteCarlo_media = g(random()) # g(U1)
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n <= 1 or sqrt(Scuad/n) > d:
        n += 1
        Ui = g(random()) # g(Ui)
        Media_Ant = MonteCarlo_media
        MonteCarlo_media = Media_Ant + (Ui - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (MonteCarlo_media - Media_Ant)**2
    print(n, sqrt(Scuad/n), 2*z_alfa_2*sqrt(Scuad/n))
    return MonteCarlo_media, Scuad, n

if __name__ == "__main__":  # Ejercicio
    for n in [1000, 10000, 100000]:
        print("Con {} simulaciones:".format(n))
        MediaI, DesvioS = monteCarlo_intervalo_sinL(g, n)
        print("Monte Carlo, I =", MediaI)
        print("Monte Carlo, S =", DesvioS)
    MediaI, DesvioS, Nsim = monteCarlo_intervalo_sinN(1.96, g, 0.003)
    print("Con {} simulaciones:".format(Nsim))
    print("Monte Carlo, I =", MediaI)
    print("Monte Carlo, S =", DesvioS)