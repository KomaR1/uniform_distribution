import matplotlib.pyplot as plt
import time
from static_function import get_bin

seed = time.time()


def lcg():
    global seed
    seed = (69069 * seed) % (2 ** 32)
    return seed


def simple_lcg(a, b):
    result_arr = [0 for i in range(b)]
    for i in range(a):
        result_arr[get_bin(lcg() / (2 ** 32), binscount=b)] += 1
    return result_arr


def draw_simple_lcg(a, b):
    y = simple_lcg(a, b)
    s = list(range(b))
    fig, ax = plt.subplots()
    plt.bar(s, y)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Метод простых конгруэнций')

    plt.show()
    fig.savefig('мой график.png')






