# Global variable
a = 10

def func():
    print(a)  # Prints message at global scope

def func():
    a = 20  # Local Variable
    print(a)


def func():
    a = 20  # a is a local variable.
    b = 20  # b is a local Variable
    return a + b


def func():
    b = 20  # Local Variable
    return a + b   # a refers to value 10 which is Global variable

def func():
    # Local Variable "a"!
    # A variable can be either local or global variable but not both
    result = a + b  # Exception! (a will not refer to Global value 10)
    a = 20
    b = 30
    result = a + b
    return result
func()

# Raises Exception!
# (UnboundLocalError: local variable 'message' referenced before assignment)

# UnboundLocalError is also caused when you try to assign a variable before assigining an initial value to it.
# Example:

def func():
    a = a + 1       # Adding 1 to un-initlised variable 'a'


def func():
    # Declaring that the variable that you are referring to is global variable
    global a  # Refers to Global Variable "a"
    a = 20
    print(a)

# Enclosing Scope
message = "universe"    # Global scope
def func():
    message = "hello"       # Enclosing scope for wrapper() and local scope for func()
    def wrapper():
        message = "world"       # Local variable to wrapper()
        print(message)
    print(message)      # Local scope
    return wrapper

"""
1. In case of classes, when you look up for an attribute "message",Python tries to look for that attribute on the instance.
2. If the attribute exist on the instance, then it will return the value of the instance attribute.
3. If the attribute does not exist on the instance, it will lookup for the attribute at class level.
4. If the attribute exist on the class level, it will return the value of the class attribute.
5. If the attribute does not exist on instance and at class level,then attribute error is raised.
"""
class Spam:
    message = "Hello world"
    def __init__(self):
        self.message = "Hello universe"

s = Spam()
print(s.message)   # Prints "Hello universe"

class Spam:
    message = "Hello world"
    def __init__(self):
        self.x = 10
        self.y = 20

s = Spam()
print(s.message)    # Prints "Hello world"

# -------------------------------------------------------------------------------------------------