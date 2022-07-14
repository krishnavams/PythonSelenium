import time

def _time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper

l = list(range(1000000))

@_time
def test_list():
    999999 in l

s = set(range(1000000))

@_time
def test_set():
    999999 in s

t = tuple(range(1000000))

@_time
def test_tuple():
    999999 in t

test_list()
test_tuple()
test_set()