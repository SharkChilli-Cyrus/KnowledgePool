import sys
import os
import time
import datetime

def test_decorator(func):
    #stored_info = "I am closure info"
    def wrapped():
        func()
        print("Decorator")
    
    return wrapped

#@test_decorator
def hello_world():
    print("Hello World")

"""
#@test_decorator
def hello_world():
    print("Hello World")

hello_world()

EQUALS TO ==>

hello_world = test_decorator(hello_world)
hello_world()
"""

# ------------------------------------------------------------
def calculate_run_time(func):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 2)

        print("INFO: Current Function [{0}] - run time is {1}".format(func.__name__, run_time))
    
    return wrapped


@calculate_run_time
def test_func(n):
    for i in range(n):
        time.sleep(0.2)
        print("Done")


if __name__ == "__main__":
    print("[1]:", hello_world.__name__)
    hello_world = test_decorator(hello_world)
    hello_world()
    print("[2]:", hello_world.__name__)


    #test_func(5)