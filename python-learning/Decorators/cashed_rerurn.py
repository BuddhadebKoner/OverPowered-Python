# implement decorator that cached the return values of the function , so that when its called with the same arguments the cached value is returend of re-rxecution the function

import time



def cached(func):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper



@cached
def long_running_func(a,b):
    time.sleep(2)
    return a + b


print(long_running_func(10,7))
print(long_running_func(50,7))
print(long_running_func(39,22))
print(long_running_func(10,7))
print(long_running_func(91,43))
