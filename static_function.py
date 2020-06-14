import matplotlib.pyplot as plt
from distributions import *


def get_bin(number, min=0.0, max=1.0, binscount=40):
    curmin = min
    curmax = max / binscount
    intIncrement = curmax
    for i in range(binscount):
        if curmin <= number < curmax:
            return i
        else:
            curmin += intIncrement
            curmax += intIncrement
    return


def draw_fun(bins_array, bins_count, title_str, min=0, max=1):

    s = list(range(min, max, int((max-min)/bins_count)))
    fig, ax = plt.subplots()
    plt.bar(s, bins_array)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title(title_str)

    plt.show()
    fig.savefig('мой график.png')


def get_rand(generator_name, distribution_name, **kwargs):
    if distribution_name == 'uniform':
        return get_uniform(generator_name, kwargs.get('min'), kwargs.get('max'))
    elif distribution_name == 'triangular':
        return get_triangular()
    elif distribution_name == 'trapezoidal':
        return get_trapezoidal()
    elif distribution_name == 'normal1':
        return get_normal1(kwargs.get('mean'), kwargs.get('deviation'))
    elif distribution_name == 'normal2':
        return get_normal2(kwargs.get('mean'), kwargs.get('deviation'))


def gen_title(generator_name, distribution_name):
    title = ''
    if distribution_name == 'uniform':
        title += 'Равномерное распределение'
    elif distribution_name == 'triangular':
        title += 'Треугольное распределение'
    elif distribution_name == 'trapezoidal':
        title += 'Трапецеидальное распределение'
    elif distribution_name == 'normal1':
        title += 'Нормальное распределение'
    elif distribution_name == 'normal2':
        title += 'Нормальное распределение 2'

    if generator_name == 'default':
        title += '\nСтандартный генератор'
    elif generator_name == 'simple':
        title += '\nМетод простых конгруэнций'
    elif generator_name == 'lemer':
        title += '\nМетод линейной конгруэнции'
    return title
