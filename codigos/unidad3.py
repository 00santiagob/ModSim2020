# Modelos y Simulacion (2020)
# Unidad 3: Generacion
# Autor: @00santiagob (GitHub)

import numpy as np
from random import random
import matplotlib.pyplot as plt


############################
# Generador de von Neumann #
############################


def vonNeumann(u):
    # Secuencia de von Neumann (1946):
    # u: debe ser un entero de hasta 4 cifras
    u = ((u**2)//100) % 10000
    return u


def ej_vonNeumann():
    # Generación de una secuencia con el generador de von Neumann
    n = 100  # longitud deseada de la secuencia
    semilla = 9999  # número entero de hasta cuatro dígitos
    secuencia = [semilla]
    for i in range(n):
        secuencia.append(vonNeumann(secuencia[i]))
    print(secuencia)
    secuencia_en_0_1 = [secuencia[i]/10000 for i in range(n)]
    print(secuencia_en_0_1)


##############################
# Generadores congruenciales #
##############################


def ranMixto(a, c, M, u):
    # Generador mixto
    # M: período, a: multiplicador, c:incremento
    # u: debe ser un entero de hasta 4 cifras
    return (a * u + c) % M


def ranMulti(a, M, u):
    # Generador multiplicativo
    # M: período, a: multiplicador
    return (a * u) % M


def ej_ranMixto():
    a = 3; c = 0; M = 7; y0 = 2
    u = y0
    rands = [u]
    for _ in range(100):
        u = (a * u + c) % M
        rands.append(u)
    print(rands[:18])
    # Grafica un histograma
    values, counts = np.unique(rands, return_counts=True)
    plt.figure(figsize=(13, 3))
    plt.vlines(values, 0, counts, color='C0', lw=4)
    plt.title('y_i = {}.y_(i-1) + {} (mod {})'.format(a, c, M))
    plt.xticks([i for i in range(M)])
    plt.ylim(0, max(counts) * 1.06)
    # Puntos en el intervalo
    xs = np.linspace(0, 1, M+1)
    ys = np.zeros(M+1)
    plt.figure(figsize=(10, 1))
    plt.title(
        'Puntos en el intervalo [0,1] al dividir la secuencia por {}'.format(M))
    plt.plot(xs, ys, '-rD', markevery=rands)
    plt.show()

# Teorema 1:
# Consideremos una secuencia dada por el generador: yn+1 = (a * yn + c) % M, con (c != 0)
# Entonces la secuencia tiene periode M <=> se cumple:
# - El maximo comun divisor entre c y M es 1: mcd(c,M)=1
# - a == 1 % p, para cualquier factor primo p de M
# - Si 4 divide a M => a == 1 % 4

def ej2_ranMixto():
    # Elegir M, a y c para obtener un generador 
    # congruencial lineal mixto que satisfaga el Teorema 1
    M = 19; a = 5; c = 3
    semilla = 0  #elegir cualquier semilla
    u = semilla
    n = 15  # longitud de la secuencia
    for _ in range(n):
        print(u,end = '    ')
        u=ranMixto(a,c,M,u)

# Si M=2**n (equivale a tomar los ultimos n bits de la representacion)
# => a = 4*m+1, y c debe ser impar.

def ej_ANSI_C():
    # Generador provisto por la biblioteca de ANSI C
    # Periodo K = 2**32 = 4.294.967.296
    M = 2**32; a = 1103515245; c = 12345
    u = 3
    rand = [u]
    for _ in range(20):
        u = ranMixto(a,c,M,u)
        rand.append(u)
    print(rand)

# Teorema 2:
# Para un generador multiplicativo yn+1 = a * yn % M
# El período K de la secuencia verifica tres propiedades:
# - Si K=M-1 entonces M es primo.
# - Si M es primo, entonces K divide a M-1.
# - K=M-1 si y sólo si a es raíz primitiva de M y M es primo.

def ej_ranMulti():
    semilla = 10
    M = 11; a = 8
    u = semilla
    secuencia = [semilla]
    for _ in range(2 * M):
        secuencia.append(ranMulti(a,M,u))
        u=ranMulti(a,M,u)
    #    print(u, end = '    ')
    print(secuencia)

def ej_Mersenne():
    # Generador congruencial multiplicativo
    # M es un primo de Mersenne de la forma 2**k-1
    # - Dado que 7 es raiz primitiva de M y (5,M-1)=1 => 7**5 es raiz primitiva
    # - Periodo K = M-1 = 2**31-2
    M = 2**31-1; a = 7**5
    n = 5 # Lungitud de secuencia
    semilla = 987654321
    u = semilla
    rand = [u]
    for _ in range(n):
        u = ranMulti(a,M,u)
        rand.append(u)
    print(rand)

def hiperplanos():
    N = 500  # Cantidad de puntos
    semilla = 987654321
    # Primer grafico
    a = 19; M = 512
    secuencia = []
    u = semilla
    for _ in range(N+1):
        secuencia.append(u)
        u = ranMulti(a,M,u)
    plt.figure(1)
    plt.title('yn=19*y{n-1} (512)',fontsize=10)
    plt.axis([0,M,0,M])
    plt.plot(secuencia[0:N],secuencia[1:N+1],'b.')
    # Segundo grafico
    a = 137; M = 256
    secuencia = []
    u = semilla
    for _ in range(N+1):
        secuencia.append(u)
        u = ranMulti(a,M,u)
    plt.figure(2)
    plt.title('yn=137*y{n-1} (256)',fontsize=10)
    plt.axis([0,M,0,M])
    plt.plot(secuencia[0:N],secuencia[1:N+1],'b.')
    # Tercer grafico
    a = 21; M = 256
    secuencia = []
    u = semilla
    for _ in range(N+1):
        secuencia.append(u)
        u = ranMulti(a,M,u)
    plt.figure(3)
    plt.title('yn=21*y{n-1} (256)',fontsize=10)
    plt.axis([0,M,0,M])
    plt.plot(secuencia[0:N],secuencia[1:N+1],'b.')
    # Cuarto grafico
    a = 21; M = 256; c = 1
    secuencia = []
    u = semilla
    for _ in range(N+1):
        secuencia.append(u)
        u = ranMixto(a,c,M,u)
    plt.figure(4)
    plt.title('yn=21*y{n-1}+1  (256)',fontsize=10)
    plt.axis([0,M,0,M])
    plt.plot(secuencia[0:N],secuencia[1:N+1],'b.')
    plt.show()

##################################################
# Generadores congruenciales lineales combinados #
##################################################

def ej_congruencial():
    u1 = 3
    u2 = 3
    lista1 = [u1]
    lista2 = [u2]
    for _ in range(42):
        # print(u1, end=', ')
        u1 = ranMixto(4,1,9,u1)
        lista1.append(u1)
    print(lista1)
    for _ in range(42):
        # print(u2, end=', ')
        u2 = ranMixto(5,3,13,u2)
        lista2.append(u2)
    print(lista2)
    cuantos = np.zeros(9)
    for j in range(36):
        cuantos[(lista1[j] + lista2[j])%9] += 1
        # print((lista1[j] + lista2[j])%9, end=', ')
    print(cuantos)

def ran0(u, M):
    'Generador ran0'
    a = 40014
    return (a*u) % M
    
def ran1(u, M):
    'Generador ran1'
    a = 40692
    return (a*u)%M
    

def ranCombinado(u1,u2, M):
    'Generador que se obtiene combinando ran0 y ran1 módulo M1 o M2'
    return (u1-u2) % M

def ej2_congruencial():
    N = 5000000
    sec1, sec2, sec3 = np.empty(N+1,float), np.empty(N+1,float), np.empty(N+1,float)
    M1 = 2**31-85
    M2 = 2**31-249
    M = M1  # se puede elegir M2 también.
    semilla1 = 1000
    semilla2 = 1000
    u1 = semilla1
    u2 = semilla2
    for i in range(N):
        u1 = ran0(u1, M1)
        u2 = ran1(u2, M2)
        u3 = ranCombinado(u1,u2, M)
        sec1[i] = u1 / M1
        sec2[i] = u2 / M2
        sec3[i] = u3 / M    
    plt.figure(1)
    plt.axis([0, 0.001, 0, 1])
    plt.title('xn=40014*x{n-1} (2**31-85)',fontsize=10)
    plt.plot(sec1[0:N],sec1[1:N+1],'b.')
    plt.figure(2) 
    plt.axis([0, 0.001, 0, 1])
    plt.title('yn=40692*y{n-1}  (2**31-249)',fontsize=10)
    plt.plot(sec2[0:N],sec2[1:N+1],'r.')
    plt.figure(3) 
    plt.axis([0, 0.001, 0, 1])
    plt.title('xn-yn  (2**31-85)',fontsize=10)
    plt.plot(sec3[0:N],sec3[1:N+1],'k.')
    plt.show()

###############################################
# Mersenne Twister de la biblioteca de Python #
###############################################

def ej_Mersenne_Twister():
    N=10000
    sec = np.empty(N+2,float)
    for i in range(N+2):
        sec[i] = random()
    plt.figure(1)
    plt.plot(sec[0 : N+1], sec[1 : N+2], 'r.', markersize = 1)
    fg = plt.figure(2)
    bx = fg.add_subplot(111, projection = '3d')
    bx.scatter(sec[1 : N+1],sec[0 : N],sec[2 : N+2], depthshade = False, s = 0.2, marker='.')
    plt.show()

if __name__ == "__main__":
    # ej_vonNeumann()
    # ej_ranMixto()
    # ej2_ranMixto()
    # ej_ANSI_C()
    # ej_ranMulti()
    # ej_Mersenne()
    # hiperplanos()
    # ej_congruencial()
    # ej2_congruencial()
    ej_Mersenne_Twister()