import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(1) #Activated before print since it's before function()
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

#Advanced decorators
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs): # Allows multiple arguments besides function
        if args[0].is_logged_in: # Takes first positional argument (user) as [0]
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_pose(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("Nii-Kwartei")
new_user.is_logged_in = True
create_blog_pose(new_user)
