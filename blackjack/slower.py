import functools
import time

def slower(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        time.sleep(0.5)
        func(*args,**kwargs)
    return wrapper
