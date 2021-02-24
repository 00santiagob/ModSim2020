# Modelos y Simulacion (2020)
# Examen Final (23/2/2021)
# Alumno: Santiago Alberto Balog

from timeit import timeit as timeit
from random import random, expovariate
from numpy import exp, log, sin, pi, zeros, sqrt
import numpy as np
import matplotlib.pyplot as plt

###############
# Ejercicio 1 #
###############

def F(x):
    if x <= 0:
        return exp(4*x)/16
    else:
        return 1/16 + x/4

def inversaX():
    U = random()
    if U < 0.0625:
        return log(U*16)/4
    else:
        return 4*U - 1/4

def ejercicio1():
    x = []
    for _ in range(1000):
        x.append(inversaX())
    print("E[X] =", sum(x)/1000)
    print("P(X <= 2) =", F(2))

###############
# Ejercicio 2 #
###############
def lamda_t(t):
    return 8*t - t**2

def ejercicio2():
    'Devuelve el numero de eventos NT y los tiempos en Eventos'
    'lamda_t(t): intensidad, lamda_t(t) <= lamda'
    T = 8
    lamda = lamda_t(T)
    NT = 0
    Eventos = []
    U = 1 - random()
    t = -log(U) / lamda
    while t <= T:
        V = random()
        if V < lamda_t(t) / lamda:
            NT += 1
            Eventos.append(t)
        t += -log(1 - random()) / lamda
    print("NT:", NT, "Eventos:", Eventos)

###############
# Ejercicio 3 #
###############

def ejercicio3():
    """
    Con parametros especificados

    H0 (Hipotesis Nula): la muestra proviene de una distribucion exponencial con media 10:
    ==> F(x) = 1 − exp(−x/10)
    """
    def F(x):
        return 1 - exp(-x/10)
    """
    ==> Los valores ordenados para una muestra de tamaño 10 para esta distribucion son:
    ==> 0.129, 1.009, 1.275, 1.314, 4.530, 5.782, 7.331, 9.416, 19.529, 32.747
    
    ¿que conclusion puede obtenerse con un nivel de rechazo del 10 %?
    ==> alfa = 0.1
    """
    Yj = [0.129, 1.009, 1.275, 1.314, 4.530, 5.782, 7.331, 9.416, 19.529, 32.747] # Valores ordenados de la muestra
    n = len(Yj) # Tamaño de la muestra
    alfa = 0.1
    d_KS = 0 # Estadistico
    print("\nEjercicio 3 - b\n")
    for j in range(1, n+1):
        FYj = F(Yj[j-1])
        izq = j/n - FYj
        der = FYj - (j-1)/n
        print(j, Yj[j-1], FYj, izq, der)
        tmp = max(izq, der)
        d_KS = max(d_KS, tmp)
    print("d_KS:", d_KS)
    pvalor = 0
    Nsim = 10000
    print("\nEjercicio 3 - c\n")
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_i= 0
        for i in range(n):
            u_i = uniformes[i]
            tmp = max((i+1)/n - u_i, u_i - i /n)
            d_i = max(d_i, tmp)
        if d_i >= d_KS:
            pvalor += 1
    pvalor = pvalor/Nsim
    print("pvalor:", pvalor)
    if pvalor < alfa:
        print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0")
    else:
        print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0")

###############
# Ejercicio 4 #
###############

def g(x): # funcion a integrar
    return ((1/x - 1)**2) *  exp(-1/x + 1) * (1/(x**2))

def monteCarlo_intervalo_sinN(z_alfa_2, L): # z_alfa_2 = z(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    print("d =", d)
    MonteCarlo_media = g(random()) # g(U1)
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n < 100 or sqrt(Scuad/n) > d:
        # print("n =", n, "sqrt(Scuad/n) =", sqrt(Scuad/n))
        n += 1
        Ui = g(random()) # g(Ui)
        Media_Ant = MonteCarlo_media
        MonteCarlo_media = Media_Ant + (Ui - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (MonteCarlo_media - Media_Ant)**2
    return round(MonteCarlo_media, 6), Scuad, n

def ejercicio4():
    print("\nEjercicio 4 - c\n")
    for L in [10**(-1), 10**(-2), 10**(-3)]:
        monteCarlo, Scuad, n = monteCarlo_intervalo_sinN(2.575, 10**(-3))
        intervalo_izq = monteCarlo - 2.575 * sqrt(Scuad/n)
        intervalo_der = monteCarlo + 2.575 * sqrt(Scuad/n)
        print("Amplitud:", L, "Nsim=", n, ":", monteCarlo, "intervalo:", "["+str(round(intervalo_izq, 6))+" ; "+str(round(intervalo_der, 6))+"]")

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

def Y(Xi, media):
    s = 0
    n = len(Xi)
    for i in range(n):
        s += (Xi[i] - media)**2
    return s

def ejercicio5():
    Xi = [3.3011, 5.6076, 4.8822, 5.6992, 5.2696, 5.4943, 3.5169, 3.9797, 4.5530, 5.1097]
    a = 3.2
    mu = promedio(Xi)
    n = 10
    Nsim = 100000
    p = 0
    for nsim in range(Nsim):
        muestra = muestra_bootstrap(Xi,n)
        y = Y(muestra, mu)
        p += (a < y)
        if nsim == 1000:
            print("Con 1000 simulaciones p = P(a < Y) =", p/1000)
    print("Con 100000 simulaciones p = P(a < Y) =", p/Nsim)


if __name__ == "__main__":
    print("\n###############\n# Ejercicio 1 #\n###############\n")
    ejercicio1()
    print("\n###############\n# Ejercicio 2 #\n###############\n")
    ejercicio2()
    print("\n###############\n# Ejercicio 3 #\n###############\n")
    ejercicio3()
    print("\n###############\n# Ejercicio 4 #\n###############\n")
    ejercicio4()
    print("\n###############\n# Ejercicio 5 #\n###############\n")
    ejercicio5()