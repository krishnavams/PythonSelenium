"""
Sets are Python's builtin data type which has the following characterstics
   1. Sets are unordered
   2. Elements inside the sets are unique
   3. Sets are mutable, but elements inside the set must be hashable
   4. Sets cannot be indexed or sliced

Hashable Objects:
Hashable objects are the objects which implements __hash__ magic method and
hash() method can be called.

All Immutable objects are hashable, but all hashable objects are not immutable

Python Sets can only include hashable objects

"""

# Operations on Set
a = {1, 2, 3, 3, 4}
print(len(a))   # Prints the Length of the Set

# Membership test
1 in a  # Prints True if the item is in a

# Set Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.union(b)  # Prints {1, 2, 3, 4, 5, 6}

c = {6, 7, 8, 9}

a.union(b, c)   # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set Intersection
a.intersection(b)   # Returns a new set {3, 4}

# Set Difference
# Returns a new set with the elements in set a which are not in b
a.difference(b)
# a - b   # Prints {1, 2}

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
a.difference(b, c)  # Returns a new set {1, 2, 3}
# a - b - c

# isdisjoint()
# Returns True if there are no items in common between two sets
x = {1, 2, 3}
y = {2, 3, 5}
x.isdisjoint(y)     # Returns False

x1 = {1, 3, 5}
x2 = {2, 4, 6}
x1.isdisjoint(x2)

# issubset()
# A set is considered a subset of another set if every element of the first set is
# in the second
a = {1}
b = {1, 2}
c = {1, 2, 3}
d = {1, 2, 4}

a.issubset(b)   # Returns True
b.issubset(c)   # Returns True
c.issubset(d)   # Returns False

# Modifying a Set add()
a = {'apple', 'yahoo', 'google'}
a.add('facebook')

# remove()
a.remove("apple")
# Element must exist in the set. Otherwise python throws key Error

# discard()
# Removes an element from the set.
# If the element does not exist, Key error is not thrown
a.discard("apple")

# pop()
# Removes and returns a random item from the set
# Throws KeyError if the set is empty
a.pop()

# clear()
# removes all the elements from the set
a.clear()

# update()
a = {1, 2}
b = {3, 4}
a.update(b)     # a = {1, 2, 3, 4}

# intersection_update()
# Modify a set by retaining only elements found in both sets
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)    # Prints {2, 3}

a = {1, 2, 3}
b = {2}
a.difference_update(b)  # Prints {1, 3}
