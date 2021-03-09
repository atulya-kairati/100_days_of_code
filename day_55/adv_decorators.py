def function_logger(function):
    def wrapper(*args, **kwargs):
        print(f'You called {function.__name__}{args} and it returned {function(*args)}')
        return function(*args)
    return wrapper


@function_logger
def test(a, b, c):
    return a*b*c


r = test(9, 8, 6)
print(f'Result is {r}')
