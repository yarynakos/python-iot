from time import time
from exceptions.defrosting_exeption import DefrostingExceptions


def check_duration_time(func):
    def timer(self):
        start_time = time() * 1000
        func(self)
        end_time = time() * 1000
        print(f'{end_time - start_time}ms')

    return timer


def convert_to_tuple(func):
    def converter(*args, **kwargs):
        return tuple(func(*args, **kwargs))

    return converter


def logged(exception, mode):
    def exception_handler(func):
        def wrapper(self):
            try:
                func(self)
            except DefrostingExceptions:
                if mode == 'console':
                    print(DefrostingExceptions.message)
                elif mode == 'file':
                    file = open('logs\\log.txt', 'a')
                    file.write(f'{DefrostingExceptions.message}\n')
                    file.close()

        return wrapper

    return exception_handler
