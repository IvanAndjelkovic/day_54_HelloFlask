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



# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f'{function.__name__} run speed:\n{end_time-start_time}')
    return wrapper_function
  
  
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    

fast_function()
slow_function()