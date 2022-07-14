# Setters and Getters
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int):
            raise TypeError()
        self._radius = value
    
    def circumference(self):
        return self._radius * 3.14 * 2
# ---------------------------------------------------------------------------------------------          
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # By setting self.first_name , the set operation uses the setter method to set the
    # first_name attribute as opposed to bypassing it by accessing self._first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First Name must be String')
        if len(value) > 12:
            raise ValueError('First Name must be less than 13 characters')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

p1 = Person('Steve', 'Jobs', 30)

print(p1.first_name)
p1.first_name = 'Bill'
print(p1.first_name)
del p1.first_name   # Raises AttributeError
# ---------------------------------------------------------------------------------------------  
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b    
    
    # internal method or private method. Should not be called directly
    # Only the methods inside this class can call this
    def _is_int(self, number):
        if not isinstance(number, int):
            raise ValueError
        return True

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
       if self._is_int(value):
            self._a = value
    
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if self._is_int(value):
            self._b = value
# ---------------------------------------------------------------------------------------------  
class Account:
    _interest = 0.04  # leading underscore indicates that balance attribute is "private"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance     

    def _spam(self):
        print("Account _spam")
    
    def demo(self):
        self._spam()
        return self._interest

class SBAccount(Account):
    _interest = 0.05        # override _interest
    def _spam(self):    # override _spam
        print("Account _spam")
# -----------------------------------------------------------------------------------------
class Account:
    __interest = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance     # leading underscore indicates that balance attribute is "private"

    def __spam(self):
        print("Account __spam")
    
    def demo(self):
        self.__spam()
        return self.__interest

class SBAccount(Account):
    __interest = 0.05        # override __interest?? NO ...
    def _spam(self):    # override __spam?? NO ....
        print("Account __spam")

# NOTE: Both single underscore and double underscore attributes can be accessed outside the class in python.
# 1.Single underscore attributes can be overriden in child class
# 2.Double underscore attributes cannot be overriden in child class
# -----------------------------------------------------------------------------------------