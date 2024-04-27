

def debugg(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kw_args = ', '.join(f"{k},{v}" for k,v in kwargs.items())
        print(f"calling : {func.__name__}, with args {args_value} and kwargs value : {kw_args}")
        return func(*args, **kwargs)

    return wrapper



@debugg
def greet(name, greeting="hello"):
    print(f"{greeting} , {name}")

@debugg
def hello():
    print("hello")


hello()
greet("chai" ,greeting="hanji")