import time # this is improted for question that given 


def timer(func):
    print(func)
    def warper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\n{func.__name__} run in {end-start} time")
        return result
    return warper

@timer
def exampleFunc(n):
    time.sleep(n)

exampleFunc(2)
