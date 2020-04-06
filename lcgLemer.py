import matplotlib.pyplot as plt
import time

seed = time.time()


def lemer_lcg():

    def lcg():
        global seed
        seed = (69069*seed+5) % (2**32)
        return seed

    fig, ax = plt.subplots()

    lcg()
    res = lcg()
    n = 10
    x = range(n)
    y = [lcg() % 1 for _ in range(n)]
    plt.bar(x, y)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Метод линейной конгурэнтной последовательности')

    plt.show()
    fig.savefig('мой график.png')
