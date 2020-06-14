import matplotlib.pyplot as plt
import random
from static_function import get_bin


def included(a, b):
    result_arr = [0 for i in range(b)]
    for i in range(a):
        result_arr[get_bin(random.uniform(0, 1), binscount=b)] += 1
    return result_arr


def draw_included(a, b):
    y = included(a, b)
    s = list(range(b))
    fig, ax = plt.subplots()
    plt.bar(s, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Метод случайных чисел на интервале')
    plt.show()
    fig.savefig('мой график.png')



