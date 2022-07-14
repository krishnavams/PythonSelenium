# Class decorators take class defnition as an argument
# Attach an attribute to the class
def attach_count(cls):
    cls.count = 0   # Creates an attribute "count" and attaches the attribute to the cls
    return cls

@attach_count       # Demo = attach_count(Demo)
class Demo:
    def spam(self):
        print("hello spam")
        self.count += 1     # Demo.count += 1
# ==================================================================================================================  
# Attaches greet function to the class
def attach_greet(cls):  
    def greet(self):
        return "hello world"
    cls.greet = greet
    return cls
# ==================================================================================================================  
@attach_greet       # Demo = greet(Demo)
class Demo:
    def spam(self):
        return "demo spam"
# ==================================================================================================================  
# Attaching a class attribute using class decorator
def prices(cls):
    print('attaching class attribute')
    # creates a class attribute by name "apple" on the class ShoppingCart
    cls.apple = {"iphone": 900, "ipad": 2800, "imac": 4500}
    return cls

@prices     # ShoppingCart = prices(ShoppingCart)
class ShoppingCart:
    def demo(self):
        print(self.apple)
# ==================================================================================================================
# Attaching an instance method to the class using class decorator
def attach_init(cls):
    def wrapper(self, a, b):
        self.a = a
        self.b = b
    cls.__init__ = wrapper
    return cls

@attach_init        # Arithmetic = attach_init(Arithmetic)
class Arithmetic:
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b   
# ==================================================================================================================
def intercept(cls):
    # Redefining the original __setattr__ method  
    def __setattr__(self, name, value):
        if value < 0:
            raise ValueError("cannot set a negative value")
        # Calling __setattr__ of object class which sets the value.
        object.__setattr__(self, name, value)
    return cls

@intercept    
class Point:  # Point = intercept(Point)
    def __init__(self, a, b):
        self.a = a
        self.b = b     
# ==================================================================================================================
# Normal function decorator.
def log(func):
    def wrapper(*args, **kwargs):
        print('Calling decorator')
        return func(*args, **kwargs)
    return wrapper

# Class decorators should take class as an argument and modified that class and returns the modified class
def logging(cls):
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, log(value))
    return cls

# All the methods inside the class will be applied with the logging decorator
@logging
class Arithmetic:       # Arithmetic = logging(Arithmetic)
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b  
# ==================================================================================================================