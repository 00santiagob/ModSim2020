def ranMixto(a, c, M, u):
    return (a * u + c) % M

def ejercicio_1b():
    n = 10
    for i in [4, 50]:
        hay_periodo = False
        periodo = 0
        y = i
        secuencia = [y]
        for _ in range(n):
            y = ranMixto(5, 4, 2**5, y)
            if y in secuencia and hay_periodo == False:
                hay_periodo = True
                periodo = len(secuencia)
            secuencia.append(y)
        print(secuencia)
        for k in range(periodo):
            if secuencia[k] == secuencia[periodo]:
                periodo = periodo - k
                print("Periodo de", i, ":", periodo)
                break

if __name__ == "__main__":
    ejercicio_1b()