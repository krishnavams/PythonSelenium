from collections import namedtuple

"""
1. Two parameters are required to create a named tuple: 
   a class name and a list of field names, which can be given as an 
   iterable of strings or as a single space- delimited string.
2. Data must be passed as positional arguments to the constructor
   (in contrast, the tuple constructor takes a single iterable).
3. You can access the fields by name or position.
4. They use less memory than a regular object because they don’t store 
   attributes in a per-instance __dict__.
"""

Employee = namedtuple("Employee", ['fname',  'lname', 'pay'])

e1 = Employee("steve", "jobs", 1000)
e2 = Employee("bill", "gates", 2000)

# Accessing values using field names
print(e1.fname)
print(e1.lname)
print(e1.pay)

# Accessing values using indexing
print(e1[0])
print(e1[1])
print(e1[2])

# length of the namedtuple
print(len(e1))
