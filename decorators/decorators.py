from time import time


def check_duration_time(func):
    def timer(self):
        start_time = time() * 1000
        func(self)
        end_time = time() * 1000
        print(f'{end_time - start_time}ms')

    return timer


def convert_to_tuple(func):
    def converter(self):
        return tuple(func(self))

    return converter
