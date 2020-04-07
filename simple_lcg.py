import matplotlib.pyplot as plt
import time

seed = time.time()


def lcg():
    global seed
    seed = (69069 * seed) % (2 ** 32)
    return seed


def simple_lcg(a, b):
    n = int(a/b)
    s = list(range(b))
    def avg(min, max, count):
        res = 0
        for i in range(count):
            if i == 0:
                i = 1
            res += lcg()
            return res/i
    y = [avg(0, 1, n) for _ in range(b)]
    fig, ax = plt.subplots()
    plt.bar(s, y)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Метод простых конгруэнций')

    plt.show()
    fig.savefig('мой график.png')






