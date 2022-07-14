"""
1. A class is collection/set of functions that carry out various operations on 
"Instances"

2. Instances are the actual objects/data that your function manipulate on.
"""
# Different ways of storing data using built-in data structures.
a = [1, 2]
t = (1, 2)
d = {'a': 1, 'b': 2}    # advantage of storing data in dict is that you can access the data via keys

# Performing different operations on the data stored in the list.
# --------------------------------------------------------------
# 1. sort 
# 2. reverse
# 3. __len__()
# 4. __getitem__()
# 5. __contains__()
# -------------------------------------------------------------
# Want to perform other operations apart from built-in
# -------------------------------------------------------------
# 1. Adding a[0] = a[0] + 0.5, a[1] = a[1] + 0.5
# 2. Get the total of two co-ordinates total = a[0] + a[1]
# 3. Swap two co-ordinates temp = a[0], a[0] = a[1], a[1] = temp
# 4. Sorting two co-ordinates a.sort()
# 5. Resetting the co-ordinates a[0] = 0, a[1] = 0
# -------------------------------------------------------------
# User defined class or datatype
class Point:
    # Data is being saved inside a dictionary
    def __init__(self, a, b):
        self.a = a
        self.b = b

p1 = Point(1, 2)
p2 = Point(10, 20)

# The values are internally stored in a dictionary. It is also called instance dictionary
print(p1.__dict__)  # {"a": 1, "b": 2}
print(p2.__dict__)  # {"a": 10, "b": 20}
# ==============================================================================================
# "Point" class with a some methods
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Takes data from instance dictionary
    def move(self, dx, dy):
        self.a += dx
        self.b += dy
    
    # resets the value of self.a and self.b to zero    
    def reset(self):
        self.a = 0
        self.b = 0
    
    # Method that sorts points
    def sort(self):
        if self.a < self.b:
            return (self.a, self.b)
        return (self.b, self.a)
    
    # Method that swaps values of 'a' and 'b'
    def swap_points(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        return (self.a, self.b)
    
    def total(self):
        return self.a + self.b
    
p1 = Point(1, 2)
p2 = Point(1.4, 1.2)

# The information about data is present in instance dictionary  (obj.__dict__)
# The information about methods is present in class dictionary (class_name.__dict__)
# ==============================================================================================
class Calculator:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

c1 = Calculator(1, 2)
c2 = Calculator(4, 5)
c3 = Calculator(10, 20)
# ==============================================================================================
# Employee Class
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'

e1 = Employee("Steve", "Jobs", 1000)
e2 = Employee("Bill", "Gates", 2000)
# ==============================================================================================
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, pts):
        self.health -= pts

p1 = Player(1, 2)
p2 = Player(3, 4)
p3 = Player(5, 6)

print(p1.__dict__)
print(p1.__class__.__dict__)
print(Player.__dict__)
# Please note that __dict__ attribute is available only for custom classes and not for builtin types!
# ==============================================================================================
class Point:
    # a and b with default values
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

p1 = Point()
p2 = Point()
# ==============================================================================================
class Employee:
    def __init__(self, fname, lname, pay, *args):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.args = args

e1 = Employee('steve', 'jobs', 1000, 'python', 26, '2200 valley view lane')
# =======================================================================================================================
# Overloading constructor using optional arguments
class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

p1 = Point()
p2 = Point(1)
p3 = Point(1, 2)
p4 = Point(1, 2, 3)
# ========================================================================================================================
# We can have multiple __init__ method's, but the latest implementation of __init__ would be considered by Python.
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Re-defining __init__ method (new implementation)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Python maintains the information about methods in class dictionary. 
# we can access the dictionary using Point.__dict__
# Method name will be the key of the dictionary and the reference of the method will be the value. 
# e.g.
# >>> Point.__dict__
# >>> mappingproxy({'__module__': '__main__', '__init__': <function Point.__init__ at 0x103ed67a0>, '__dict__': <attribute '__dict__' of 'Point' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None})

# when you have multiple method's with the same name, the key of the class dictionary will be overwritten.
# So the new reference of the function object (with new implementation) would be stored in the class dictionary.
# Point.__dict__
# >>> mappingproxy({'__module__': '__main__', '__init__': <function Point.__init__ at 0x102282830>, '__dict__': <attribute '__dict__' of 'Point' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None})
# ===================================================================================================================================