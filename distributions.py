import random
import time
from scipy.stats import trapz

seed = time.time()
seed2 = time.time() % 2**30


def lcgS():
    global seed
    seed = (69069 * seed) % (2 ** 32)
    return seed


def lcgL():
    global seed2
    seed2 = (69069 * seed2 + 5) % (2 ** 32)
    return seed2


def get_uniform(genname, min, max):
    if genname == 'default':
        return random.uniform(min, max)
    elif genname == 'lemer':
        return lcgL() / (2 ** 32)
    elif genname == 'simple':
        return lcgS() / (2 ** 32)


def get_triangular():
    return random.triangular()


def get_trapezoidal():
    return trapz.rvs(0.2, 0.8, size=1)[0]

def get_normal1(mean, deviation):
    result = random.gauss(mean, deviation)
    print(result)
    print(type(result))
    return random.gauss(mean, deviation)

def get_normal2(mean, deviation):
    return random.normalvariate(mean, deviation)
