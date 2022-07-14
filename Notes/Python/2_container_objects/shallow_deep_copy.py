"""
Two types of copy operations are applied to container objects such as lists and dictionaries:
a shallow copy and a deep copy. 
A shallow copy creates a new object, but populates it with references to the same items contained in the original object.
"""

a = [1, 2, [10, 20]]

# create a copy of a
b = a.copy()

# "a" and "b" are pointing to two different objects
print(a is b) # False

a.append(3)  # 3 is appended to the list "a" but not to list "b"

a[2].append(30)     # 30 gets appeneded to the internal list, which is shared by both "a" and "b"

print(a)    # [1, 2, [10, 20, 30]]
print(b)    # [1, 2, [10, 20, 30]]

# A deep copy creates a new object and copies all the objects it contains.
from copy import deepcopy
a = [1, 2, [10, 20]]
b = deepcopy(a)

print(a is b)       # False

a[2].append(30)     # a = [1, 2, [10, 20, 30]]

print(b)        # b = [1, 2, [10, 20]] 