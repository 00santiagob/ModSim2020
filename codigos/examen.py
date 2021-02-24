# Modelos y Simulacion (2020)
# Examen Final (9/2/2021)
# Autor: 00santiagob

from timeit import timeit as timeit
from random import random, expovariate
from numpy import exp, log, sin, pi, zeros, sqrt
import numpy as np
import matplotlib.pyplot as plt

###############
# Ejercicio 1 #
###############

def exponencial(lamda):
    U = 1 - random()
    return -log(U) / lamda

def ejercicio1():
    Nsim = 10000 # Cantidad de Simulaciones
    lamda = [0.1, 0.15, 0.2] # lamda de cada caja
    CantidadXv = 0 # número de veces que el mínimo coincide con el valor de la exponencial que corresponde al tren verde
    TiempoPromedio = 0 # Promedio de todos los mínimos
    XvMenorQueXn = 0 # veces que el valor de la exponencial "verde" es menor que el valor de la "naranja"
    for _ in range(Nsim):
        exponenciales = []
        for i in range(3):
            exponenciales.append(exponencial(lamda[i]))
        Xmin = min(min(exponenciales[0], exponenciales[1]), exponenciales[2])
        if Xmin == exponenciales[1]:
            CantidadXv += 1
        TiempoPromedio += Xmin
        if exponenciales[1] < exponenciales[0]:
            XvMenorQueXn += 1
    CantidadXv /= Nsim
    TiempoPromedio /= Nsim
    XvMenorQueXn /= Nsim
    print('c) I) La probabilidad de que el primer tren que llegue a la estacion sea el verde es:', CantidadXv)
    print('c) II) El tiempo promedio que transcurre hasta que llega alguno de los subtes es:', TiempoPromedio)
    print('c) III) La probabilidad de que el primer tren verde llegue antes que el primer tren naranja es:', XvMenorQueXn)

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
    pvalor = 0
    for _ in range(Nsim):
        datos = zeros(n, int) # Muestras
        N = zeros(k, int) # Frecuencias observadas
        psubi = zeros(k, float) # Probabilidades p_sub_i
        # Genera la muestra de tamaño 100 con distribucion geometrica
        for j in range(n):
            datos[j] = geometrica(p_sombrero)
        # Genera las frecuencias observadas
        N *= 0
        for observacion in datos:
            if observacion <= k-1:
                N[observacion-1] += 1
            else:
                N[k-1] += 1
        # Calcula p(sim): como p es desconocido lo estimamos con los datos de la muestra
        p = len(datos) / sum(datos)
        q = 1 - p
        # Calcula las probabilidades p_sub_i
        for i in range(k-1):
            psubi[i] = p * (q**(i))
        psubi[k-1] = 1 - sum(psubi)
        # Calcula el estadistico T
        T = 0
        for i in range(k):
            arriba = (N[i] - (n * psubi[i]))**2
            abajo = (n * psubi[i])
            T += arriba / abajo
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
    print("\nEjercicio 4 - c\n")
    for Nsim in [1000, 10000, 100000]:
        monteCarlo, Scuad = monteCarlo_intervalo_sinL(1.96, Nsim)
        intervalo_izq = monteCarlo - 1.96 * Scuad / sqrt(Nsim)
        intervalo_der = monteCarlo + 1.96 * Scuad / sqrt(Nsim)
        print("Nsim=", Nsim, ":", monteCarlo, "intervalo:", "["+str(intervalo_izq)+" ; "+str(intervalo_der)+"]")
    print("\nEjercicio 4 - d\n")
    monteCarlo, Scuad, n = monteCarlo_intervalo_sinN(1.96, 0.01)
    intervalo_izq = monteCarlo - 1.96 * Scuad / sqrt(n)
    intervalo_der = monteCarlo + 1.96 * Scuad / sqrt(n)
    print("Nsim=", n, ":", monteCarlo, "intervalo:", "["+str(intervalo_izq)+" ; "+str(intervalo_der)+"]")


###############
# Ejercicio 5 #
###############

def muestra_bootstrap(Xi,n):
    muestra = []
    lenXi = len(Xi)
    for _ in range(n):
        u = int(random() * lenXi)
        muestra.append(Xi[u])
    return muestra
         
def promedio(Xi):
    return sum(Xi)/len(Xi)

def Scuadrado(Xi):
    s = 0
    n = len(Xi)
    media = promedio(Xi)
    for i in range(n):
        s += (Xi[i] - media)**2
    s /= n-1
    return s

def ejercicio5():
    Xi = [142, 33, 54, 67, 122, 9, 44, 78, 86, 133, 22]
    a, b = -50, 50
    sigma = Scuadrado(Xi)
    n = 11
    Nsim = 1000
    p = 0
    for _ in range(Nsim):
        muestra = muestra_bootstrap(Xi,n)
        S = Scuadrado(muestra)
        p += ((a < (S - sigma)) and ((S - sigma) < b))
    print("p = P(a < S^2 - Sigma^2 < b) =", p/Nsim)

if __name__ == "__main__":
    print("\n###############\n# Ejercicio 1 #\n###############\n")
    ejercicio1()
    print("\n###############\n# Ejercicio 3 #\n###############\n")
    ejercicio3()
    print("\n###############\n# Ejercicio 4 #\n###############\n")
    ejercicio4()
    print("\n###############\n# Ejercicio 5 #\n###############\n")
    ejercicio5()