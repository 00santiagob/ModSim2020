# Modelos y Simulacion (2020)
# Examen Final (9/2/2021)
# Alumno: Santiago Alberto Balog

from timeit import timeit as timeit
from random import random
from numpy import exp, log, sin, pi, zeros, sqrt
import numpy as np
import matplotlib.pyplot as plt

###############
# Ejercicio 1 #
###############

'No llegue'

###############
# Ejercicio 3 #
###############

def geometrica(p):  
    '''simulando ensayos Bernoulli hasta obtener un éxito'''
    i = 0
    while True:
        i += 1
        if random() < p:
            return i

def ejercicio3():
    Nsim = 500 # Cantidad de simulaciones que se haran
    n = 100 # Tamaño de la muestra
    k = 4
    p_sombrero = 0.5988 # 0.598802395
    t0 = 2.72799813
    datos = zeros(n, int) # Muestras
    N = zeros(k, int) # Frecuencias observadas
    psubi = zeros(k, float) # Probabilidades p_sub_i
    pvalor = 0
    for _ in range(Nsim):
        # Genera la muestra de tamaño 100 con distribucion geometrica
        for j in range(n):
            datos[j] = geometrica(p_sombrero)
        # Genera las frecuencias observadas
        N *= 0
        for observacion in datos:
            if observacion < k-1:
                N[observacion] += 1
            else:
                N[k-1] += 1
        # Calcula p(sim): como p es desconocido lo estimamos con los datos de la muestra
        p = len(datos) / sum(datos)
        # Calcula las probabilidades p_sub_i
        for i in range(1,k-1):
            psubi[i] = p * (1 - p)**(i-1)
        psubi[k-1] = 1 - sum(psubi)
        # Calcula el estadistico T
        T = 0
        for i in range(k):
            arriba = (N[i] - n * psubi[i])**2
            abajo = (n * psubi[i])
            T +=  arriba / abajo
        if T >= t0:
            pvalor +=1
    pvalor = pvalor/Nsim
    print("pvalor:", pvalor)
    alfa = 0.05
    if pvalor < alfa:
        print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0")
    else:
        print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0")

###############
# Ejercicio 4 #
###############

def g(x): # funcion a integrar
    return ((pi**2) * x * sin(x * 3 * pi / 4)) / 16

def monteCarlo_intervalo_sinL(z_alfa_2, Nsim): # z_alfa_2 = z(alfa/2)
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

def monteCarlo_intervalo_sinN(z_alfa_2, L): # z_alfa_2 = z(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    MonteCarlo_media = g(random()) # g(U1)
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n < 100 or sqrt(Scuad/n) > d:
        n += 1
        Ui = g(random()) # g(Ui)
        Media_Ant = MonteCarlo_media
        MonteCarlo_media = Media_Ant + (Ui - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (MonteCarlo_media - Media_Ant)**2
    return MonteCarlo_media, Scuad, n

def ejercicio4():
    print("Ejercicio 4 - c")
    for Nsim in [1000, 10000, 100000]:
        monteCarlo, Scuad = monteCarlo_intervalo_sinL(1.96, Nsim)
        intervalo_izq = monteCarlo - 1.96 * Scuad / sqrt(Nsim)
        intervalo_der = monteCarlo + 1.96 * Scuad / sqrt(Nsim)
        print("Nsim=", Nsim, ":", monteCarlo, "intervalo:", "["+str(intervalo_izq)+" ; "+str(intervalo_der)+"]")
    print("Ejercicio 4 - d")
    monteCarlo, Scuad, n = monteCarlo_intervalo_sinN(1.96, 0.01)
    intervalo_izq = monteCarlo - 1.96 * Scuad / sqrt(n)
    intervalo_der = monteCarlo + 1.96 * Scuad / sqrt(n)
    print("Nsim=", n, ":", monteCarlo, "intervalo:", "["+str(intervalo_izq)+" ; "+str(intervalo_der)+"]")


###############
# Ejercicio 5 #
###############

'No llegue'

if __name__ == "__main__":
    # ejercicio3()
    ejercicio4()