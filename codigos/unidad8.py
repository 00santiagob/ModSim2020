# Modelos y Simulacion (2020)
# Unidad 8
# Autor: @00santiagob (GitHub)

from numpy import zeros, exp, log
import numpy as np
from math import factorial
from random import random, uniform

######################################
# Tecnicas de Validacion Estadistica #
######################################

# Pruebas de bondad de ajuste

'Datos discretos con parametros no especificados - Test Chi-Cuadrado'

def Poisson(lamda):
    '''Funcion Auxiliar'''
    '''Método de transformada inversa'''
    U = random() 
    i = 0; p = exp(-lamda)
    F = p
    while U >= F:
        i += 1        
        p *= lamda / i
        F = F + p
    return i

def chi_cuadrado():
    """
    Ejemplo 8.2: A lo largo de 30 dias han habido:
        6 dias => 0 accidentes
        2 dias => 1 accidentes
        1 dias => 2 accidentes
        9 dias => 3 accidentes
        7 dias => 4 accidentes
        4 dias => 5 accidentes
        1 dias => 8 accidentes

    H0 (Hipotesis Nula): Los datos provienen de X ~ Poisson(lamda)
    
    ==> lamda_sombrero = E[X] = (6*0 + 2*1 + 1*2 + 9*3 + 7*4 + 4*5 + 1*8) / 30 = 2.9

    Como una poisson puede tomar infinitos numeros
    ==> agrupamos los que sean >= 5
    ==> k = {0,..,6}

    ==> N0 = 6; N1 = 2; N2 = 1; N3 = 9; N4 = 7; N5 = 5

    Ahora tenemos que Psubi = exp(-2.9) * 2.9^i / i! para i = {0,..,4}
    ==> Psub5 = 1 - (Sum(Psubi))
    ==> Los p sub i se calculan a mano

    El Estadistico muestral T (t0) = Sum((Ni - n * Psubi)**2 / (n * Psubi)) = 19.887012

    """
    Nsim = 10000 # Cantidad de simulaciones que se haran
    n = 30 # Tamaño de la muestra
    k = 6
    lamda_sombrero = 2.9
    t0 = 19.887012
    datos = zeros(n, int) # Muestras
    N = zeros(k, int) # Frecuencias observadas
    p = zeros(k, float) # p(sim) - Probabilidades p_sub_i
    pvalor = 0
    for _ in range(Nsim):
        # Genera la muestra de tamaño 30 con distribucion de Poisson
        for j in range(n):
            datos[j] = Poisson(lamda_sombrero)
        # Genera las frecuencias observadas
        N *= 0
        for observacion in datos:
            if observacion < k-1:
                N[observacion] += 1
            else:
                N[k-1] += 1
        # Calcula lamda(sim): como lamda es desconocido lo estimamos con los datos de la muestra
        lamda = sum(datos) / len(datos)
        # Calcula las probabilidades p_sub_i
        for i in range(5):
            p[i] = exp(-lamda) * lamda**i / factorial(i)
        p[k-1] = 1 - sum(p)
        # Calcula el estadistico T
        T = 0
        for i in range(6):
            T += (N[i] - n * p[i])**2 / (n * p[i])
        if T >= t0:
            pvalor +=1
    pvalor = pvalor/Nsim
    print("pvalor:", pvalor)
    alfa = 0.01
    if pvalor < alfa:
        print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0")
    else:
        print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0")


'Datos continuos - Test de Kolmogorov-Smirnov'

def kolmogorov_smirnov():
    """
    Ejemplo 8.3: Con parametros especificados

    H0 (Hipotesis Nula): la muestra proviene de una distribucion exponencial con media 100:
    ==> F(x) = 1 − exp(−x/100)
    """
    def F(x):
        return 1 - exp(-x/100)
    """
    ==> Los valores ordenados para una muestra de tamaño 10 para esta distribucion son:
    ==> 55,72,81,94,112,116,124,140,145,155
    
    ¿que conclusion puede obtenerse con un nivel de rechazo del 5 %?
    ==> alfa = 0.05
    """
    Yj = [55, 72, 81, 94, 112, 116, 124, 140, 145, 155] # Valores ordenados de la muestra
    # Si no estan ordenados, se ordenan
    n = len(Yj) # Tamaño de la muestra
    alfa = 0.05
    d_KS = 0 # Estadistico
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

def kolmogorov_smirnov2():
    """
    Ejemplo 8.4: Con parametros NO especificados

    H0 (Hipotesis Nula): la muestra proviene de una distribucion exponencial con media desconocida:
    ==> F(x) = 1 − exp(−x/lamda)
    """
    def F_exponencial(x, lamda):
        'Distribucion acumulada de la exponencial'
        return 1 - exp(-x*lamda)
    """
    ==> Los valores ordenados para una muestra de tamaño 10 para esta distribucion son:
    ==> 55,72,81,94,112,116,124,140,145,155
    
    ¿que conclusion puede obtenerse con un nivel de rechazo del 5 %?
    ==> alfa = 0.05
    """
    Yj = [55, 72, 81, 94, 112, 116, 124, 140, 145, 155] # Valores ordenados de la muestra
    # Si no estan ordenados, se ordenan
    n = len(Yj) # Tamaño de la muestra
    alfa = 0.05
    media = sum(Yj) / n
    lamda = 1/media
    d_KS = 0 # Estadistico
    for j in range(1, n+1):
        FYj = F_exponencial(Yj[j-1], lamda)
        izq = j/n - FYj
        der = FYj - (j-1)/n
        print(j, Yj[j-1], FYj, izq, der)
        tmp = max(izq, der)
        d_KS = max(d_KS, tmp)
    print("d_KS:", d_KS)
    Nsim = 10000
    # Paso 1: Simular el pvalor con uniformes
    pvalor = 0
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
    if -2 < (pvalor - alfa) and (pvalor - alfa) < 2:
        print("Como el pvalor es cercano al", alfa*100, "%, hacemos una segunda simulacion")
        # Paso 2: Simular el pvalor con la distribucion que le coresponde
        pvalor = 0
        for _ in range(Nsim):
            muestra = []
            for _ in range(n):
                muestra.append(-log(1 - random()) / lamda)
            muestra.sort()
            lamda_est = n/sum(muestra)
            d_i= 0
            for i in range(n):
                u_i = F_exponencial(muestra[i], lamda_est)
                tmp = max((i+1)/n - u_i, u_i - i /n)
                d_i = max(d_i, tmp)
            if d_i >= d_KS:
                pvalor += 1
        pvalor = pvalor/Nsim
        print("pvalor con exponencial:", pvalor)
        if pvalor < alfa:
            print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0")
        else:
            print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0")
    else:
        if pvalor < alfa:
            print("Para un nivel de rechazo del", alfa*100, "%, se rechaza H0")
        else:
            print("Para un nivel de rechazo del", alfa*100, "%, no se puede rechazar H0")

# El problema de las dos muestras

'Test de suma de rangos para n y m pequeños'

def rangos(n, m, r):
    # pvalor = 2 * min(rangos(n,m,r), 1-rangos(n,m,r-1))
    if n == 1 and m == 0:
        if r < 1:
            p = 0.
        else:
            p = 1.
    elif n==0 and m == 1:
        if r < 0:
            p = 0.
        else:
            p = 1.
    else:
        if n == 0:
            p = rangos(0,m-1,r)
        elif m == 0:
            p = rangos(n-1,0,r-n)
        else: # n > 0, m > 0
            p = (n * rangos(n-1, m, r-n-m) + m * rangos(n, m-1, r)) / (n+m)
    return p

def suma_rangos_pvalor(r, Nsim):
    """
    H0: X = [x1, x2,..., xn]; Y = [y1, y2,..., ym] provienen de la misma distribucion F
    ==> consideramos: y1 = x_n+1, ... , ym = x_n+m

    Todos los ordenamientos de menor a mayor son igualmente probables
    ==> XY = X + Y (concatenacion)
    ==> XY = [x1, ... , xn, x_n+1, ... , x_n+m]
    ==> Ordenamos XY
    """
    pmas, pmenos = 0, 0
    for _ in range(Nsim):
        a = [i for i in range(1, n+m+1)] # Generamos valores de {1,..,n+m}
        # Generamos una permutacion de a
        N = len(a)
        for j in range(N-1):
            indice = int((N-1) * random()) + j
            a[j], a[indice] = a[indice], a[j]
        # Calculamos los rangos de los xi desde 1 hasta n
        Rangos = [a.index(i) for i in range(1, n+1)]
        s = sum(Rangos)
        if s >= r:
            pmas += 1
        if s <= r:
            pmenos += 1
    # Retornamos el pvalor
    return 2 * min(pmas, pmenos) / Nsim

if __name__ == "__main__":
    # chi_cuadrado()
    # kolmogorov_smirnov()
    # kolmogorov_smirnov2()
    pass