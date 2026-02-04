import time

## Python Decorator
def delay_decorator(function):
    def wrapper_function():
        #do something before the function
        time.sleep(2)
        function()
        function()
        # do something after the function
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

def say_buy():
    print("buy")

def say_greeting():
    print("How Are you")

say_hello()