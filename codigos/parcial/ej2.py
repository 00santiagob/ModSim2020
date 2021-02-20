import numpy as np
from random import random


def generarX_TI():  # Ejercicio 2-a)
    U = random()
    if U < 0.40:
        return 4
    elif U < 0.7:
        return 3
    elif U < 0.9:
        return 2
    else:
        return 1


def generarX_AR():  # Ejercicio 2-b)
    p = [0.1, 0.2, 0.3, 0.4]
    while True:
        Y = int(4 * random()) + 1
        U = random()
        if U < p[Y - 1] / (1.6 * 0.25):
            return Y


def Media_Muestral_X(N, generarX):  # Auxiliar para el ejercicio 2-c)
    Media = generarX()  # X(1)
    n = 1
    while n <= N:
        n += 1
        Xn = generarX()
        Media_Ant = Media
        Media = Media_Ant + (Xn - Media_Ant)/n
    return Media


if __name__ == "__main__":  # Ejercicio 2-c)
    for n in [100, 1000, 10000, 100000]:
        print("Con {} simulaciones:".format(n))
        MediaTI = Media_Muestral_X(n, generarX_TI)
        print("Transformada Inversa Media(X) =", MediaTI)
        MediaAR = Media_Muestral_X(n, generarX_AR)
        print("Aceptacion y Rechazo Media(X) =", MediaAR)
