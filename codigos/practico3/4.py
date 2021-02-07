from random import random, expovariate

def seleccionar_caja():
    # Elegir una caja basado en un número aleatorio entre 0 y 1
    # y en las probabilidades que tiene cada caja de ser elegida
    caja = random()
    if caja <= 0.4:
        return 1
    elif caja <= 0.72:
        return 2
    else:
        return 3

if __name__ == '__main__':
    Nsim = 1000 # cantidad de iteraciones
    lamda = [1/3, 1/4, 1/5] # lamda de cada caja
    espera_mayor_4 = 0
    espera_menor_4 = 0
    n_uso_caja = [0,0,0]
    for _ in range(Nsim):
        caja = seleccionar_caja()
        espera = expovariate(lamda[caja - 1])
        espera_mayor_4 += (espera > 4)
        espera_menor_4 += (espera <= 4)
        n_uso_caja[caja - 1] += (espera > 4)
    print('4) a) La probabilidad de que el cliente espere menos de 4 minutos es :', espera_menor_4/Nsim)
    for i in range(3):
        print('4) b) La probabilidad de que el cliente haya elegido la caja', i+1,
              'dado que esperó mas de 4 minutos es', n_uso_caja[i]/espera_mayor_4)