import time

def _time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper

@_time
def test_tuple():
    for i in range(1000000):
        pass

@_time
def test_list():
    for i in range(1000000):
        pass

test_list()
test_tuple()