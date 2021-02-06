# Modelos y Simulacion (2020)
# Unidad 6
# Autor: @00santiagob (GitHub)

from random import random
from numpy import exp, log
import numpy as np

################################################
# Generacion de variables aleatorias continuas #
################################################

# Metodo de la Transformada Inversa

def InversaX(G):
    U = random()
    return G(U) # G = F^-1

# Calcula la Raiz n-ezima a partir del maximo

def raizn(n):
    Maximo = 0
    for _ in range(n):
        Maximo = max(Maximo, random())
    return Maximo

###############
# Exponencial #
###############

def exponencial1():
    U = 1 - random()
    return -log(U)

def exponencial2(lamda):
    return exponencial1() / lamda

###########
# Poisson #
###########

def poisson_con_exp(lamda):
    X = 0
    Producto = 1 - random()
    cota = exp(-lamda)
    while Producto >= cota:
        Producto *= 1 - random()
        X += 1
    return X

#########
# Gamma #
#########

def gamma(n, lamda):
    U = 1
    for _ in range(n):
        U *= 1 - random()
    return -log(U) / lamda

def dosExp(lamda):
    t = gamma(2, lamda)
    U = random()
    X = t * U
    Y = t - X
    return X, Y

def nExp(n, lamda):
    t = gamma(n, lamda)
    unif = random.uniform(0, 1, n-1)
    unif.sort()
    exponenciales = [unif[0] * t]
    for i in range(n-2):
        exponenciales.append((unif[i+1] - unif[i]) * t)
    exponenciales.append((1 - unif[n-2]) * t)
    return exponenciales

##################################
# Metodo de Aceptacion y Rechazo #
##################################

def Aceptacion_Rechazo_X(f, g, c):
    while True:
        Y = random() # Generar Y ~ Uniforme(0,1)
        U = random()
        if U < f(Y) / (c * g(Y)): # No se el valor de c
            return Y # aceptacion: X = Y
        # rechazo: vuelve a generar otra Y

# Ejemplo:
# f(y) = 20 * y * (1 - y)**3    si 0 <= y <= 1
# g(y) = 1                      si 0 <= y <= 1
# f(y)/g(y) = f(y) ==> f'(y) = 20 * (1-y)**2 * (1-4y)
# f'(y) = 0 cuando y = 1/4 (PUNTO CRITICO)
# c = f(1/4)/g(1/4) = f(1/4) = 135/64 = 2.109375
# ==> f(y)/(c*g(y)) = 20 * 64/135 * y * (1 - y)**3
#                   = 9.481481 * y * (1 - y)**3
# ==> Podemos cambiar la condicion del if de la funcion anterior
# por if U < 9.481481 * y * (1 - y)**3

###############################################
# Simulacion de variables aleatorias normales #
###############################################

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

# Metodo Polar

def MetodoPolar(): # Asi aparece en el video
    Rcuadrado = -2 * log(1 - random()) # R^2 ~ Exponencial(1/2)
    Theta = 2 * np.pi * random() # Theta ~ Uniforme(0, 2*Pi)
    X = np.sqrt(Rcuadrado) * np.cos(Theta)
    Y = np.sqrt(Rcuadrado) * np.sin(Theta)
    return (X, Y)

def MetodoPolar_con_MuSigma(mu, sigma): # Asi aparece en el apunte
    Rcuadrado = -2 * log(1 - random())
    Theta = 2 * np.pi * random()
    X = np.sqrt(Rcuadrado) * np.cos(Theta)
    Y = np.sqrt(Rcuadrado) * np.sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)

# Transformaciones de Box-Muller

def Polar_Box_Muller(mu, sigma):
    # Generar un punto aleatorio en el circulo unitario.
    while True:
        # V1 y V2 van entre [-1; 1]
        V1, V2 = 2 * random() - 1, 2 * random() - 1
        S = V1 ** 2 + V2 ** 2 # S ~ Uniforme(0, 1)
        if S <= 1:
            X = V1 * np.sqrt(-2 * log(S) / S)
            Y = V2 * np.sqrt(-2 * log(S) / S)
            return (X * sigma + mu, Y * sigma + mu)

# Metodo de Razon entre Uniformes

def normalvariate(mu, sigma):
    NV_MAGICCONST = 4 * exp(-0.5) / np.sqrt(2.0)
    while True:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
    return mu + z * sigma

#######################################
# Generacion de un Proceso de Poisson #
#######################################

# Proceso de Poisson Homogeneo

def eventosPoisson(lamda, T):
    t = 0
    NT = 0
    Eventos = []
    U = 1 - random()
    while t < T:
        t += -log(U) / lamda
        if t <= T:
            NT += 1
            Eventos.append(t - log(U) / lamda)
    return NT, Eventos

# Proceso de Poisson NO Homogeneo

def Poisson_no_homogeneo_adelgazamiento(lamda_t, lamda, T):
    'Devuelve el numero de eventos NT y los tiempos en Eventos'
    'lamda_t(t): intensidad, lamda_t(t) <= lamda'
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
    return NT, Eventos

# Ejemplo: Proceso de Poisson No Homogeneo
# funcion de intensidad lamda_t(t) = 2*t + 1 si 0 <= t <= 6
# Subdividimos el intervalo [0:6] => I1 = [0:2], I2 = (2:4], I3 = (4:6]
# Acotamos lamda_t(t) => lamda_t(2) = 5 = lamda1
#                        lamda_t(4) = 9 = lamda2
#                        lamda_t(6) = 13 = lamda3

def Poisson_adelgazamiento_mejorado(T):
    interv = [2, 4, 6] # T <= 6
    lamda = [5, 9, 13]
    j = 0 # Recorre subintervalos
    NT = 0
    Eventos = []
    U = 1 - random()
    t = -log(U) / lamda[j]
    while t <= T:
        if t <= interv[j]:
            V = random()
            if V < (2*t + 1) / lamda[j]:
                NT += 1
                Eventos.append(t)
            t += -log(1 - random()) / lamda[j]
        else: # t > interv[j]
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j+1]
            j += 1
    return NT, Eventos

###############################################
# Metodo de aceptacion y rechazo transformado #
###############################################

'Este tema no entro al examen, pero se puede ver en la guia.'

if __name__ == "__main__":
    pass