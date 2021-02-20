# Modelos y Simulacion (2020)
# Unidad 7
# Autor: @00santiagob (GitHub)

from random import random
from numpy import sqrt
import numpy as np

###############################
# Estimacion con simulaciones #
###############################

def Media_Muestral_X(d):
    'Estimacion del valor esperado con ECM < d'
    Media = simular X # X(1)
    Squad, n = 0, 1 # Scuad = S^2(1)
    while n <= 100 or sqrt(Scuad/n) > d:
        n += 1
        simular X
        Media_Ant = Media
        Media = Media_Ant + (X - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (Media - Media_Ant)**2
    return Media

def estimador_p(d):
    'Estimacion de proporcion con ECM < d'
    p = 0
    n = 0
    while n <= 100 o sqrt(p * (1-p) / n) > d:
        n += 1
        simular X
        p = p + ( X - p) / n
    return p

############################
# Estimacion por intervalo #
############################

def Media_Muestral_X_interv(z_alfa_2, L): # z_alfa_2 = z(alfa/2)
    'Confianza = (1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    Media = simular X # X(1)
    Scuad, n = 0, 1 # Scuad = S^2(1)
    while n <= 100 or sqrt(Scuad/n) > d:
        n += 1
        simular X
        Media_Ant = Media
        Media = Media_Ant + (X - Media_Ant) / n
        Scuad = Scuad * (1 - 1/(n-1)) + n * (Media - Media_Ant)**2
    return Media

def estimador_p_interv(z_alfa_2, L): # z_alfa_2 = z(alfa/2)
    'Confianza = 100(1 - alfa)%, amplitud del intervalo: L'
    d = L / (2 * z_alfa_2)
    p = 0
    n = 0
    while n <= 100 o sqrt(p * (1-p) / n) > d:
        n += 1
        simular X
        p = p + ( X - p) / n
    return p

if __name__ == "__main__":
    pass