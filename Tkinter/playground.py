total = 0

# *args allows any number of arguments in parameters, referred by position
def add(*args):
    print(args[0]) #since args is a tuple, elements can be accessed as such. Position matters
    total = 0
    for n in args:
        total += n
    return total

print(add(1,3,5,7,4,4,6))