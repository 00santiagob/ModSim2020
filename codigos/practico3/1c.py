from sympy.ntheory import factorint
from math import gcd

def esPeriodoM(a,c,M):
    if gcd(c,M) != 1:
        return False
    factors = factorint(M)
    for x in factors:
        if (a % x) != 1:
            return False
    if M % 4 == 0:
        return (a % 4 == 1)
    return True

def checkPrimeNumber(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                isPrime = False
                break
        isPrime = True
    return isPrime

def ejercicio_1c(a, c, M):
    if c != 0:
        if esPeriodoM(a,c,M):
            print("El periodo es Maximo:", M)
        else:
            print("El periodo no es Maximo")
    else:
        if checkPrimeNumber(M):
            print("El periodo es Maximo:", M-1)
        else:
            print("El periodo no es Maximo")

if __name__ == "__main__":
    a = [125,123,5,7]
    c = [3,3,0,0]
    M = [2**9,2**9,71,71]
    for i in range(4):
        ejercicio_1c(a[i], c[i], M[i])
