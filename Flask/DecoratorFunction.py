import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2) #Activated before print since it's before function()
        function()
        function()
    return wrapper_function

# Using decorator function to delay print
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you")

say_hello()

# Alternative to activate
decorated_function = delay_decorator(say_greeting)
decorated_function()