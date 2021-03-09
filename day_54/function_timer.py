import time

num = 10000000


def my_function_timer(function):

    def wrapper():
        i_time = time.time()

        function()

        e_time = time.time()
        delta = e_time - i_time
        print("-" * 30)
        print(f"{function.__name__} took {delta} secs to run.")
        print("-" * 30)

    return wrapper


@my_function_timer
def fast_sum():
    print(sum(list(range(num))))


@my_function_timer
def slow_sum():
    s = 0
    for i in range(num):
        s += i
    print(s)


fast_sum()
slow_sum()
