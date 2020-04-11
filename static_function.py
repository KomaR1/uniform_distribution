

def getBin(number, min=0.0, max=1.0, binscount=40):
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