from random import random

def do():
    U = random()
    if U < 1.0 / 3.0:
        W = random() + random()
        return (W <= 2)
    else:
        W = random() + random() + random()
        return (W <= 2)

if __name__ == "__main__":
    ns = [100, 1000, 10000, 100000, 1000000]
    for n in ns:
        k = 0
        for _ in range(n):
            k += do()
        k /= n
        print(k)