def vonNeumann(u):
    # Secuencia de von Neumann (1946):
    # u: debe ser un entero de hasta 4 cifras
    u = ((u**2)//100) % 10000
    return u

def ejercicio_1a():
    n = 10
    for semilla in [3792,1004,2100,1234]:
        secuencia = [semilla]
        for i in range(n):
            secuencia.append(vonNeumann(secuencia[i]))
        print(secuencia)

if __name__ == "__main__":
    ejercicio_1a()