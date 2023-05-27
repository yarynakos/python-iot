from datetime import datetime


def check_duration_time(func):
    def timer(self):
        start_time = datetime.now()
        func(self)
        end_time = datetime.now()
        print(end_time - start_time)
    return timer
