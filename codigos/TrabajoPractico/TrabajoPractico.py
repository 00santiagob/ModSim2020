# Modelos y Simulacion (2020)
# Trabajo Practico Especial
# Autor: 00santiagob

from random import random, seed
from numpy import log, zeros, mean, std
from queue import Queue
import matplotlib.pyplot as plt

#######################################
##                                   ##
##  Trabajo Practico para el Examen  ##
##                                   ##
#######################################

# Funciones Auxiliares

def exponencial(lamda):
    'Genera v.a continua Exponencial'
    U = 1 - random()
    return -log(U) / lamda

def eventosPoisson(lamda, T):
    'Proceso de Poisson Homogeneo'
    seed(1024) # Semilla para poder repetir la simulacion
    t = 0
    NT = 0
    Eventos = []
    while NT < T:
        U = 1 - random()
        t += -log(U) / lamda
        Eventos.append(t)
        NT += 1
    return Eventos

def insertarDatosNuevos(ProximoCliente, datosActualizados):
    lugarEnLaFila = 0
    while lugarEnLaFila < len(ProximoCliente):
        if datosActualizados[0] < ProximoCliente[lugarEnLaFila][0]:
            ProximoCliente.insert(lugarEnLaFila, datosActualizados)
            return
        lugarEnLaFila += 1
    ProximoCliente.append(datosActualizados)
    return

###############
# Ejercicio 1 #
###############

"""
Hay dos cajeros automaticos
Al llegar un cliente puede ocurrir que ambos cajeros esten ocupados
==> el cliente se forma en una fila a esperar:
        que alguno de los dos cajeros se desocupe y entonces el cliente
        utiliza el cajero que se desocupe primero
Los clientes llegan de acuerdo a un Proceso de Poisson con tasa Lamda = 6 clientes por minutos
TS1: Tiempo de Servicio del cajero 1, tiene densidad exponencial con razon lamda = 4 minutos
TS2: Tiempo de Servicio del cajero 2, tiene densidad exponencial con razon lamda = 3 minutos
TS1 y TS2 son V.A. Independientes del proceso de arribo de los clientes a la cola
"""

def ej1_a(nClientes, NC, TS1, TS2):
    Cajero1, Cajero2 = True, True # Ambos cajeros empiezan estando disponibles
    FilaDeEspera = Queue()
    uso_de_cajero1 = 0 # Cantidad de clientes que usaron el cajero 1
    TiemposDeUso = zeros(nClientes) # Tiempo que el cliente i-esimo utilizo el servicio
    LlegadaDeCliente = eventosPoisson(NC, nClientes) # Simulo la llegada de los n Clientes
    # Contiene a los proximos clientes que debe procesar el sistema
    ProximoCliente = [(LlegadaDeCliente[i], i, "espera") for i in range(nClientes)]
    # Primero esta el tiempo en que sucede la accion
    # Segundo estan los identificadores de los clientes
    # Tercero estan los estados en que los clientes pueden estar: "espera", "cajero1", "cajero2"
    # Los clientes inician siempre en "espera" aunque sea el primero
    while len(ProximoCliente):
        tiempo, cliente, estado = ProximoCliente[0]
        if estado == "espera":
            FilaDeEspera.put(cliente)
        # Si el cliente abandona algun cajero se calcula cuanto tiempo estuvo en el sistema
        elif estado == "cajero1":
            TiemposDeUso[cliente] = tiempo - LlegadaDeCliente[cliente] # Guardo el tiempo que paso en el cajero 1
            Cajero1 = True # Marco al cajero 1 como disponible
        else:
            TiemposDeUso[cliente] = tiempo - LlegadaDeCliente[cliente] # Guardo el tiempo que paso en el cajero 2
            Cajero2 = True # Marco al cajero 1 como disponible
        if FilaDeEspera.qsize(): # Implica que hay clientes esperando para usar un cajero
			# Chequeo que haya algun cajero disponible, empezando por el cajero 1
            if Cajero1:
                Cajero1 = False # Se ocupa el cajero 1
                datosActualizados = (tiempo + exponencial(TS1), FilaDeEspera.get(), "cajero1")
                # Inserto los nuevos datos del cliente de manera que queden ordenados por tiempo
                insertarDatosNuevos(ProximoCliente, datosActualizados)
                uso_de_cajero1 += 1
            elif Cajero2:
                Cajero2 = False # Se ocupa el cajero 2
                datosActualizados = (tiempo + exponencial(TS2), FilaDeEspera.get(), "cajero2")
                # Inserto los nuevos datos del cliente de manera que queden ordenados por tiempo
                insertarDatosNuevos(ProximoCliente, datosActualizados)
        ProximoCliente.remove(ProximoCliente[0]) # Se elimina los datos viejos del cliente
    # Retorno la proporcion de personas que usaron el cajero 1 y el tiempo que cada cliente uso el sistema
    return (uso_de_cajero1 / nClientes), TiemposDeUso

def ej1_b(usos_de_cajero1, TiemposDeUso):
    # Realizo una simulacion de 1000 clientes
    print('El tiempo medio que el cliente pasa en el sistema es:', mean(TiemposDeUso))
    print('Su correspondiente desviacion estandar es:', std(TiemposDeUso))
    print('La proporcion de clientes atendidos por el cajero 1 es:', usos_de_cajero1)

def ej1_c(TiemposDeUso):
    bin = [0.5 * i for i in range(16)]
    plt.style.use('dark_background')
    plt.hist(TiemposDeUso, bins=bin, edgecolor='red', color='green', alpha=0.8)
    plt.xlabel('Tiempo de espera')
    plt.ylabel('Cantidad de clientes')
    plt.title('Ejercicio 1')
    plt.show()

###############
# Ejercicio 2 #
###############

"""
Suponemos ahora que cada cajero tiene su propia cola de espera
Al llegar un cliente, se forma en el que tiene menos clientes esperando
Si ambas filas tienen igual cantidad de clientes ==> se forma en la fila del cajero 1
"""
def ej2_a(nClientes, NC, TS1, TS2):
    Cajero1, Cajero2 = True, True # Ambos cajeros empiezan estando disponibles
    FilaCajero1 = Queue()
    FilaCajero2 = Queue()
    uso_de_cajero1 = 0 # Cantidad de clientes que usaron el cajero 1
    TiemposDeUso = zeros(nClientes) # Tiempo que el cliente i-esimo utilizo el servicio
    LlegadaDeCliente = eventosPoisson(NC, nClientes) # Simulo la llegada de los n Clientes
    # Contiene a los proximos clientes que debe procesar el sistema
    ProximoCliente = [(LlegadaDeCliente[i], i, "espera") for i in range(nClientes)]
    # Primero esta el tiempo en que sucede la accion
    # Segundo estan los identificadores de los clientes
    # Tercero estan los estados en que los clientes pueden estar: "espera", "cajero1", "cajero2"
    # Los clientes inician siempre en "espera" aunque sea el primero
    while len(ProximoCliente):
        tiempo, cliente, estado = ProximoCliente[0]
        if estado == "espera":
            if FilaCajero1.qsize() < FilaCajero2.qsize():
                FilaCajero1.put(cliente)
            elif FilaCajero1.qsize() > FilaCajero2.qsize():
                FilaCajero2.put(cliente)
            else:
                if Cajero1 or (not Cajero1 and not Cajero2):
                    FilaCajero1.put(cliente)
                else:
                    FilaCajero2.put(cliente)
        # Si el cliente abandona algun cajero se calcula cuanto tiempo estuvo en el sistema
        elif estado == "cajero1":
            TiemposDeUso[cliente] = tiempo - LlegadaDeCliente[cliente] # Guardo el tiempo que paso en el cajero 1
            Cajero1 = True # Marco al cajero 1 como disponible
        else:
            TiemposDeUso[cliente] = tiempo - LlegadaDeCliente[cliente] # Guardo el tiempo que paso en el cajero 2
            Cajero2 = True # Marco al cajero 1 como disponible
        # Chequeo que haya clientes esperando en la fila 1 y que este disponible el cajero 1
        if FilaCajero1.qsize() and Cajero1:
            Cajero1 = False # Se ocupa el cajero 1
            datosActualizados = (tiempo + exponencial(TS1), FilaCajero1.get(), "cajero1")
            # Inserto los nuevos datos del cliente de manera que queden ordenados por tiempo
            insertarDatosNuevos(ProximoCliente, datosActualizados)
            uso_de_cajero1 += 1
        # Chequeo que haya clientes esperando en la fila 2 y que este disponible el cajero 2
        if FilaCajero2.qsize() and Cajero2:
            Cajero2 = False # Se ocupa el cajero 2
            datosActualizados = (tiempo + exponencial(TS2), FilaCajero2.get(), "cajero2")
            # Inserto los nuevos datos del cliente de manera que queden ordenados por tiempo
            insertarDatosNuevos(ProximoCliente, datosActualizados)
        ProximoCliente.remove(ProximoCliente[0])# Se elimina los datos viejos del cliente
    # Retorno la cantidad de personas que usaron el cajero 1 y el tiempo que cada cliente uso el sistema
    return (uso_de_cajero1 / nClientes), TiemposDeUso

def ej2_b(TiemposDeUso):
    # Realizo una simulacion de 1000 clientes
    print('El tiempo medio que el cliente pasa en el sistema es:', mean(TiemposDeUso))
    print('Su correspondiente desviacion estandar es:', std(TiemposDeUso))

def ej2_c(nClientes, usos_de_cajero1):
    print('La proporcion de clientes atendidos por el cajero 1 es:', usos_de_cajero1)

#################
# Funcion Extra #
#################

def ej_extra_hist2(TiemposDeUso2):
    bin = [0.5 * i for i in range(16)]
    plt.style.use('dark_background')
    plt.hist(TiemposDeUso2, bins=bin, edgecolor='yellow', color='blue', alpha=0.8)
    plt.xlabel('Tiempo de espera')
    plt.ylabel('Cantidad de clientes')
    plt.title('Ejercicio 2')
    plt.show()

def ej_extra_comp(TiemposDeUso, TiemposDeUso2):
    bin = [0.5 * i for i in range(16)]
    plt.style.use('dark_background')
    plt.hist(TiemposDeUso, bins=bin, edgecolor='red', fc='None')
    plt.hist(TiemposDeUso2, bins=bin, edgecolor='yellow', fc='None')
    plt.xlabel('Tiempo de espera')
    plt.ylabel('Cantidad de clientes')
    plt.title('Comparacion de ambos Ejercicios')
    plt.show()

if __name__ == "__main__":
    nClientes = 10000
    NC, TS1, TS2 = 6, 4, 3
    # EJERCICIO 1
    print("Ejercicio 1")
    usos_de_cajero1, TiemposDeUso = ej1_a(nClientes, NC, TS1, TS2)
    ej1_b(usos_de_cajero1, TiemposDeUso)
    ej1_c(TiemposDeUso)
    # EJERCICIO 2
    print("Ejercicio 2")
    usos_de_cajero1, TiemposDeUso2 = ej2_a(nClientes, NC, TS1, TS2)
    ej2_b(TiemposDeUso2)
    ej2_c(nClientes, usos_de_cajero1)
    # EXTRA
    ej_extra_hist2(TiemposDeUso2)
    ej_extra_comp(TiemposDeUso, TiemposDeUso2)