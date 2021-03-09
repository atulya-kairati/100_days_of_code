# args
def add(*args):
    return sum(args)


# kwargs
def name_marks(**kwargs):
    print(kwargs)


class Car:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'pota')
        self.model = kwargs.get('model', 'pota')
        self.power = kwargs.get('power', 'pota')

    def __str__(self):
        return f'Car Name:{self.name}\nModel:{self.model}\nPower:{self.power}'


print(add(2, 34, 2, 123, 4623, 45))
name_marks(ramu=34, shamu=45)
car = Car(model='&WH', name='LEAF', power='440')
print(car)


