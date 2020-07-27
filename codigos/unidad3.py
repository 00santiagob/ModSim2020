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
    a = 3
    c = 0
    M = 7
    y0 = 2
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


def ej2_ranMixto():
    # Elegir M, a y c para obtener un generador 
    # congruencial lineal mixto que satisfaga el Teorema 1
    M = 19
    a = 5
    c = 3
    semilla = 0  #elegir cualquier semilla
    u = semilla
    n = 15  # longitud de la secuencia
    for _ in range(n):
        print(u,end = '    ')
        u=ranMixto(a,c,M,u)


if __name__ == "__main__":
    ej_vonNeumann()
    # ej_ranMixto()
