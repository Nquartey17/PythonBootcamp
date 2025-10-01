total = 0

# *args allows any number of arguments in parameters, referred by position
def add(*args):
    print(args[0]) #since args is a tuple, elements can be accessed as such. Position matters
    total = 0
    for n in args:
        total += n
    return total

# print(add(1,3,5,7,4,4,6))

#Create keyword arguments to use in dictionary
def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"]) #get value by name
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") #kw["make"] - using get prevents errors if value is empty
        self.model = kw.get("model") # kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
my_car = Car(make="Nissan")
print(my_car.model)