# Modelos y Simulacion (2020)
# Unidad 5
# Autor: @00santiagob (GitHub)

from numpy import exp, log
import numpy as np
from random import random
import matplotlib.pyplot as plt
from timeit import timeit as timeit
from scipy.stats import binom

################################################
# Simulación de variables aleatorias discretas #
################################################

# Probabilidades
# p(1) = 0.20 , p(2) = 0.15 , p(3) = 0.25 , p(4) = 0.40

# TI : Transformada Inversa

def TInversa_sin_ordenar(u):
    if u < 0.20:
        return 1
    elif u < 0.35:
        return 2
    elif u < 0.60:
        return 3
    else:
        return 4

# Ordenamiento de las probabilidades de mayor a menor
# p(4) = 0.40 , p(3) = 0.25 , p(1) = 0.20 , p(2) = 0.15

def TInversa_ordenados(u):
    if u  < 0.40:
        return 4
    elif u < 0.65:
        return 3
    elif u < 0.80:
        return 1
    else:
        return 2

# Medición de tiempos de ejecución

def ej_CompTiempos1():
    n = 100
    no_ordenados = [0] * n
    ordenados = [0] * n
    for u in range(n):
        mycode = "TInversa_sin_ordenar("+str(u/n)+")"
        no_ordenados[u] = timeit(mycode, number = 100000, globals = globals())
        mycode = "TInversa_ordenados("+str(u/n)+")"
        ordenados[u] = timeit(mycode, number = 100000, globals = globals())
    fig, ax = plt.subplots(figsize = (15,3))
    ax.plot(no_ordenados, 'r', label = 'sin ordenar')
    ax.plot(ordenados, 'b', label = 'ordenados')
    ax.set_xticks([i for i in range(0,101,20)])
    ax.set_xticklabels([str(i/5.) for i in range(6)])
    ax.set_xlabel('u')
    ax.set_ylabel('tiempo por ejecución')
    ax.legend(loc = 'best')
    plt.suptitle('Comparación de tiempos de corrida')
    plt.show()

############
# Uniforme #
############

def udiscreta1(n):
    U = random()
    x = 1
    F = 1/n
    while U >= F:
        F += 1/n
        x += 1
    return x

def udiscreta2(n):
    U = random()
    return int(n * U) + 1

def udiscreta3(m,k):
    U = random()
    return int(U * (k-m+1)) + m

# Permutacion añeatoria de un conjunto de cardinal N

def permutacion1(a): # a = [a[0], a[1], ... , a[N-1]]
    N = len(a)
    for j in range(N-1):
        indice = int((N-1) * random()) + j
        a[j], a[indice] = a[indice], a[j]
    return a

def permutacion2(a):
    N = len(a)
    for j in range(N-1, 0, 1):
        indice = int((j-1) * random())
        a[j], a[indice] = a[indice], a[j]
    return a

## Devuelve un subconjunto aleatorio de A de r elementos

def subcAleatorio(r,A):
    N = len(A)
    for j in range(N-1, N-1-r, -1):
        indice = int((j+1) * random())
        A[j], A[indice] = A[indice], A[j]
    return A[N-r:]

############
# Promedio #
############

def ej_5_2():
    Suma = 0
    Nsim = 100
    for _ in range(Nsim):
        U = int(random() * 10000) + 1
        Suma += exp(1 / U)
    return Suma / Nsim * 10000

############
# Binomial #
############

def Binomial1(n,p):
    'Método de transformada inversa'
    i = 0
    c = p / (1-p)
    prob = (1-p) ** n
    F = prob
    U = random()
    while U >= F:
        prob = c * (n-i) / (i+1) * prob
        F= F + prob 
        i = i + 1
    return i

def Binomial2(n, p):
    'Método de TI seleccionando p < 0.5'
    'Optimizado'
    if p > 0.5:
        return n - Binomial1(n, 1-p)
    else:
        return Binomial1(n, p)

# Medición de tiempos de ejecución

def ej_CompTiempos2():
    n = 100
    bin1 = [0] * n
    bin2 = [0] * n
    N = 100000
    for p in range(1,n):
        mycode = "Binomial1(15,"+str(p/n)+")"
        bin1[p] = timeit(mycode, globals = globals(), number = N)
        mycode = "Binomial2(15,"+str(p/n)+")"
        bin2[p] = timeit(mycode, globals = globals(), number = N)
    fig, ax = plt.subplots(figsize = (15,4))
    ax.plot(bin1, 'r', label = 'Binomial normal')
    ax.plot(bin2, 'b', label = 'Binomial selectiva')
    ax.set_xlabel('p')
    ax.set_ylabel('tiempo por ejecución')
    ax.set_xticks([i for i in range(0,101,20)])
    ax.set_xticklabels([str(i/5.) for i in range(6)])
    ax.legend(loc = 'best')
    ax.set_title('Binomial(15, p)')
    plt.suptitle('Comparación de tiempos de corrida')
    plt.show()

def tasas_riesgo_binomial(n, p):
    t_riesgo = np.empty((n+1))
    probs = np.asarray([binom(n,p).pmf(i) for i in range(n+1)])
    condicional = 1.
    for i in range(n+1):
        t_riesgo[i] = probs[i] / condicional
        condicional -= probs[i]
    return t_riesgo

def Binomial_TR(n, p, t_riesgo):
    x = 0
    while True:
        U = random()
        if U < t_riesgo[x]:
            return x
        else:
            x += 1

# Medición de tiempos de ejecución

def ej_CompTiempos3():
    n = 100
    bin1 = [0] * n
    bin2 = [0] * n
    bin3 = [0] * n
    N = 10000
    for p in range(1,n):
        mycode = "Binomial1(15,"+str(p/n)+")"
        bin1[p] = timeit(mycode, globals = globals(), number = N)
        mycode = "Binomial2(15,"+str(p/n)+")"
        bin2[p] = timeit(mycode, globals = globals(), number = N)
        t_riesgo = tasas_riesgo_binomial(15,p/n) # t_riesgo es una lista
        mycode = "Binomial_TR(15,"+str(p/n)+","+str(t_riesgo)+")"
        bin3[p] = timeit(mycode, globals = globals(), number = N)
    fig, ax = plt.subplots(figsize = (15,4))
    ax.plot(bin1, 'r', label = 'Binomial normal')
    ax.plot(bin2, 'b', label = 'Binomial selectiva')
    ax.plot(bin3, 'g', label = 'Binomial Tasas de riesgo')
    ax.set_xlabel('p')
    ax.set_ylabel('tiempo por ejecución')
    ax.set_xticks([i for i in range(0,101,20)])
    ax.set_xticklabels([str(i/5.) for i in range(6)])
    ax.legend(loc = 'best')
    ax.set_title('Binomial(15, p)')
    plt.suptitle('Comparación de tiempos de corrida')
    plt.show()

##############
# Geometrica #
##############

def geom1(p):  
    '''aplicando Transformada inversa'''
    q = 1-p
    F = p
    i = 1
    U = random()
    while U >= F:
        p *= q
        F += p
        i += 1
    return i

def geom2(p):  
    ''' utilizando log(1-U) / log(1-p)'''
    U = random()
    return int(log(1-U) / log(1-p)) + 1

def geom3(p):
    '''simulando ensayos Bernoulli hasta obtener un éxito'''
    i = 0
    while True:
        i += 1
        if random() < p:
            return i

# Medición de tiempos de ejecución

def ej_CompTiempos4():
    n = 100
    metodo1 = [0] * 100
    metodo2 = [0] * 100
    metodo3 = [0] * 100
    for p in range(1, n):
        metodo1[p] = timeit("geom1("+str(p/n)+")", globals = globals(), number = 10000)
        metodo2[p] = timeit("geom2("+str(p/n)+")", globals = globals(), number = 10000)
        metodo3[p] = timeit("geom3("+str(p/n)+")", globals = globals(), number = 10000)
    fig, ax1 = plt.subplots(figsize = (15,3))
    ax1.plot(metodo1, 'r', label = 'Transformada Inversa')
    ax1.plot(metodo2, 'b', label = 'int(log(1-U)/log(1-p)) + 1')
    ax1.plot(metodo3, 'g', label = 'Simulando Bernoullis')
    ax1.set_xticks([i for i in range(0,101,20)])
    ax1.set_xticklabels([str(i/5.) for i in range(6)])
    ax1.set_xlabel('p')
    ax1.set_ylabel('tiempo por ejecución')
    ax1.set_title('Métodos de simulación de geométricas')
    ax1.legend(loc = 'best')
    plt.show()

#############
# Bernoulli #
#############

def bernoulli(p):
    U = random()
    if U < p:
        return 1
    else:
        return 0

def nBernoullis(N,p):
    Bernoullis = np.zeros(N, dtype=int)
    j = geom2(p) - 1
    while j < N:
        Bernoullis[j] = 1
        j += geom2(p)
    return Bernoullis

###########
# Poisson #
###########

def Poisson(lamda):
    '''Método de transformada inversa'''
    U = random() 
    i = 0; p = exp(-lamda)
    F = p
    while U >= F:
        i += 1        
        p *= lamda / i
        F = F + p
    return i

def Poisson_ordenado(lamda):
    I = int(lamda)
    p = exp(-lamda)
    F = p
    ## Cálculo de F(I)
    for i in range(1,I+1):
        p *= lamda / i
        F += p
    U = random()
    if U >= F: #recorre I, I+1, I+2, ...
        while U >= F:
            I += 1
            p *= lamda/I
            F += p
        return I
    else:
        while U < F: #recorre I-1, I-2, ...
            F -= p
            p *= I / lamda
            I -= 1
        return I + 1
    
def Poisson_con_exp(lamda):
    X = 0
    Producto = 1 - random()
    cota = exp(-lamda)
    while Producto >= cota:
        Producto *= 1 - random()
        X += 1
    return X

# Medición de tiempos de ejecución

def ej_CompTiempos5():
    metodo_TI = []
    metodo_TIordenado = []
    metodo_exp = []
    for lamda in range(1, 100):
        metodo_TI.append( timeit("Poisson("+str(lamda)+")", globals = globals(), number = 10000))
        metodo_TIordenado.append( timeit("Poisson_ordenado("+str(lamda)+")", globals = globals(), number = 10000))
        metodo_exp.append( timeit("Poisson_con_exp("+str(lamda)+")", globals = globals(), number = 10000))
    for lamda in range(100, 300, 10):
        metodo_TI.append( timeit("Poisson("+str(lamda)+")", globals = globals(), number = 10000))
        metodo_TIordenado.append( timeit("Poisson_ordenado("+str(lamda)+")", globals = globals(), number = 10000))
        metodo_exp.append( timeit("Poisson_con_exp("+str(lamda)+")", globals = globals(), number = 10000))
    fig, [ax1, ax2] = plt.subplots(nrows = 1, ncols = 2, figsize = (15,4))
    ax1.plot(metodo_TI[:100], 'b', label = 'Transformada inversa')
    ax1.plot(metodo_TIordenado[:100], 'g', label = 'Probs ordenadas')
    ax1.plot(metodo_exp[:100], 'r', label = 'con exponenciales')
    #ax.set_xticks([i for i in range(0,101,20)])
    ax1.set_xlabel('lambda')
    ax1.set_ylabel('tiempo por ejecución')
    ax1.set_title('Métodos de simulación de Poisson')
    ax1.legend(loc = 'best')
    ax2.plot(metodo_TI[100:], 'b', label = 'Transformada inversa')
    ax2.plot(metodo_TIordenado[100:], 'g', label = 'Probs ordenadas')
    ax2.plot(metodo_exp[100:], 'r', label = 'con exponenciales')
    ax2.set_xticklabels([str((i-1) * 25  + 100) for i in range(9)])
    #ax2.set_xticks([i + 100 for i in range(0,101,20)])
    ax2.set_xlabel('lambda')
    ax2.set_ylabel('tiempo por ejecución')
    ax2.set_title('Métodos de simulación de Poisson')
    ax2.legend(loc = 'best')

##################################
# Metodo de Aceptacion y Rechazo #
##################################

def Rechazo_X(p, q, c):
    while True:
        # X toma valores en {1,...,10}
        Y = int(10 * random()) + 1 # Generar xj
        U = random()
        if U < p[Y] / (c * q[Y]): # No se el valor de c
            return Y # aceptacion: X = Y
        # rechazo: vuelve a generar otra Y

#########################
# Metodo de Composicion #
#########################

def composicion1(n, alfa):
    U = random()
    if U < alfa: # Generar X1
        return int(random() * n/2) + 1
    else: # Generar X2
        return int(random() * n/2) + n/2 + 1

###################
# Metodo de Alias #
###################

# Se hacen calculos a mano para obtener las probabilidades que comparamos con U

def alias(): # No me convencio del Teorico
    # Si X toma valores em {1, 2, 3, 4} ==> n = 4
    U = random()
    k = 3 # n-1 
    XI = int(U * k) + 1
    # n-1 condicionales: X1, X2, ... , Xn-1
    if XI == 1:
        if U < 5/8:   return 1
        else:         return 3
    elif XI == 2:
        if U < 9/16:  return 4
        else:         return 2
    else: # XI == 3
        if U < 11/16: return 1
        else:         return 2

if __name__ == "__main__":
    # ej_CompTiempos1()
    # ej_CompTiempos2()
    # ej_CompTiempos3()
    # ej_CompTiempos4()
    ej_CompTiempos5()