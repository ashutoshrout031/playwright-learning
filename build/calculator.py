from functools import reduce
import math as mt

def add(*a):
    r = sum(a)
    return r

def subtract(*a):
    if not a:
        return 0
    return reduce(lambda x,y: x-y,a)

def multiplication(*a):
    if not a:
        return 0
    r = mt.prod(a)
    return r

def div_int(a,b):
    if b==0:
        raise ValueError("Can't Divisible by 0")
    return a//b








