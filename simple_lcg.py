import matplotlib.pyplot as plt
import time

seed = time.time()


def main_simple_lcg():
    def simple_lcg():
        global seed
        seed = (4093*seed+150889) % 714025
        return seed

    fig, ax = plt.subplots()

    simple_lcg()
    res = simple_lcg()
    n = 10
    x = range(n)
    y = [simple_lcg() % 1 for _ in range(n)]
    plt.bar(x, y)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Метод линейной конгурэнтной последовательности')

    plt.show()
    print(y)

    fig.savefig('мой график.png')
