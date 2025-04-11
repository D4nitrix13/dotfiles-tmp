from random import random


def my_function(a: int, b: int) -> None:
    if a > b:
        print('A es mayor')
    else:
        print('B es mayor')
    return a + b
