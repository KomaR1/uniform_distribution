import matplotlib.pyplot as plt
import random


def included():
    n = 10
    x = range(n)
    y = [random.uniform(0, 1) for _ in range(n)]
    fig, ax = plt.subplots()
    plt.bar(x, y)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Генерация случайных чисел на интервале')

    plt.show()
    fig.savefig('мой график.png')

