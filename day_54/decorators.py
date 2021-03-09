

def my_decorator(function):
    print("My decorator function")

    def wrapper_function():
        print("wrapper function")
        function()

    return wrapper_function


@my_decorator
def say_hi():
    print("Hi mothafukas")


def say_hello():
    print("Hello mothafukas")


say_hi()
# or
decorated_hello = my_decorator(say_hello)
decorated_hello()