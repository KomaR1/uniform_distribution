import matplotlib.pyplot as plt
import time
from static_function import getBin

seed = time.time() % 2**30


def lcgL():
    global seed
    seed = (69069 * seed + 5) % (2 ** 32)
    return seed


def lemer_lcg(a, b):
    result_arr = [0 for i in range(b)]
    for i in range(a):
        result_arr[getBin(lcgL() / (2 ** 32), binscount=b)] += 1
    return result_arr


def draw_lemer_lcg(a, b):
    y = lemer_lcg(a, b)
    s = list(range(b))
    fig, ax = plt.subplots()
    plt.bar(s, y)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Метод линейной конгруэнции')

    plt.show()
    fig.savefig('мой график.png')
