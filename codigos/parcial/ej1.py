import numpy as np
from numpy import sqrt, log
from random import random
from scipy.stats import norm

def abs_Z(): # Genera |Z|
    while True:
        X = -log(1 - random())
        U = -log(1 - random())
        if U >= (X - 1) ** 2 / 2:
            return X

def Normal_composicion(): # Simula Z ~ Normal(0, 1)
    Y = abs_Z() # Y = |Z|
    if random() < 0.5:
        return Y
    else:
        return -Y

# Metodo de aceptacion y rechazo para una normal

def Normal_rechazo(mu, sigma): # Simula X ~ Normal(mu, sigma)
    # X = sigma * Z + mu
    return Normal_composicion() * sigma + mu

def Media_Scuad(datos, N):
    media = datos[0]
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n < N:
        n += 1
        Ui = datos[n-1]
        Media_Ant = media
        media = Media_Ant + (Ui - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (media - Media_Ant)**2
    return media, sqrt(Scuad)

def ej1_b(Yj, mu, sigma):
    'Estadıstico de Kolmogorov Smirnov'
    d_KS = 0 # Estadistico
    for j in range(1, n+1):
        fi = (Yj[j-1]-mu)/sigma
        FYj = norm.cdf(fi)
        izq = j/n - FYj
        der = FYj - (j-1)/n
        print(j, Yj[j-1], fi, FYj, izq, der)
        tmp = max(izq, der)
        d_KS = max(d_KS, tmp)
    print("d_KS:", d_KS)
    return d_KS

def ej1_c(d_KS, n, mu, sigma, Normal_rechazo):
    pvalor = 0
    n = 20
    Nsim = 10000
    for _ in range(Nsim):
        datos = []
        for _ in range(n):
            datos.append(Normal_rechazo(mu, sigma)) #creando muestra de datos
        datos.sort()
        d_j = 0 # Estadistico
        for j in range(1, n+1):
            FYj = norm.cdf((Yj[j-1]-mu)/sigma)
            izq = j/n - FYj
            der = FYj - (j-1)/n
            tmp = max(izq, der)
            d_j = max(d_j, tmp)
        if d_j >= d_KS:
            pvalor += 1
    pvalor = pvalor/Nsim
    print("pvalor con normal:", pvalor)
    return pvalor

def ej1_d(d_KS, n):
    pvalor = 0
    Nsim = 10000
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
    print("pvalor con uniformes:", pvalor)
    return pvalor

if __name__ == "__main__":
    # Valores ordenados de la muestra
    Yj = [4.51, 6.19, 3.99, 2.79, 5.26, 5.30, 4.04, 5.37, 4.69, 6.68, 3.55, 3.43, 4.02, 4.16, 7.58, 5.11, 1.99, 3.00, 2.67, 2.61]
    # Si no estan ordenados, se ordenan
    Yj.sort()
    n = len(Yj) # Tamaño de la muestra
    alfa = 0.01

    'Estimacion de Mu y Sigma'
    # Opcion 1: forma iterativa
    # mu, sigma = Media_Scuad(Yj, n)
    # Opcion 2: Como se haria en el teorico
    mu = sum(Yj) / n
    sigma = 0
    for i in range(20):
        sigma += (Yj[i] - mu)**2
    sigma /= n-1
    sigma = sqrt(sigma)
    print("Mu:", mu, "Sigma:", sigma)
    d_KS = ej1_b(Yj, mu, sigma)
    print("Ejercicio C")
    pvalor_normal = ej1_c(d_KS, n, mu, sigma, Normal_rechazo)
    print("Ejercicio D")
    pvalor_uniforme = ej1_d(d_KS, n)

    if -2 < (pvalor_uniforme - alfa) and (pvalor_uniforme - alfa) < 2:
        print("Como el pvalor con distribucion uniforme es cercano al", alfa*100, "%, habria que hacer una segunda simulacion. Ya se hizo en el inciso C")
        if pvalor_normal < alfa:
            print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0 con una distribucion normal")
        else:
            print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0 con una distribucion normal")
    else:
        if pvalor_uniforme < alfa:
            print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0 con una distribucion uniforme")
        else:
            print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0 con una distribucion uniforme")