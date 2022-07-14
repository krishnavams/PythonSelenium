from functools import singledispatch, singledispatchmethod

@singledispatch
def add(a, b):
    print("base function add")

@add.register(int)
def _(a, b):
    print("int")
    return a + b

@add.register(float)
def _(a, b):
    print("float")
    return 0.00

@add.register(list)
def _(a, b):
    print("list")
    return sum(a) + b

class Arithmetic:
    @singledispatchmethod
    def add(a, b):
        print("base function add")

    @add.register(int)
    def _(a, b):
        print("int")
        return a + b

    @add.register(float)
    def _(a, b):
        print("float")
        return 0.00

    @add.register(list)
    def _(a, b):
        print("list")
        return sum(a) + b

# =================================================================    
from multipledispatch import dispatch
# =================================================================
@dispatch(int, int)
def add(a, b):
    print("int and int")
    return a + b

@dispatch(int, float)
def add(a, b):
    print("int and float")
    return a + b

# =================================================================
@dispatch(list, str)
def concatenate(a, b):
    a.append(b)
    return a

@dispatch(str, str)
def concatenate(a, b):
    return a + b

@dispatch(str, int)
def concatenate(a, b):
    return a + str(b)
# =================================================================