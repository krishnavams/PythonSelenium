import tracemalloc
# -------------------------------------------------------------------------------------------
def make_tuple(row):
    """Constructs a tuple from a list"""
    return (float(row[0], float(row[1], float(row[2]))))
# -------------------------------------------------------------------------------------------
def make_dict(row):
    """Constructs a dictionary from a list"""
    return {"x": float(row[0]), "y": float(row[1]), "z": float(row[2])}
# -------------------------------------------------------------------------------------------
class Point:
    """Creats an instance of class"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
# -------------------------------------------------------------------------------------------
def make_class_instance(row):
    """Creates an instance of Point class"""
    return Point(float(row[0], float(row[1]), float(row[2])))
# -------------------------------------------------------------------------------------------
def memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return result
    return wrapper
# -------------------------------------------------------------------------------------------
@memory
def from_file():
    data = [ ]
    with open("points.txt") as f:
        for line in f:
            parts = line.split()
            data.append(make_class_instance(parts))
    return data

data = from_file()
# -------------------------------------------------------------------------------------------
# Calculate Average of x, y and z co-ordinates
x_total = y_total = z_total = 0
for item in data:
    x_total += item.x
    y_total += item.y
    z_total += item.z

average = (x_total/len(data), y_total/len(data), z_total/len(data))
# -------------------------------------------------------------------------------------------
# Calculate Minimum of x, y and z co-ordinates
x_min = y_min = z_min = 0
for item in data:
    x_min = min([ item.x for item in data ])
    y_min = min([ item.y for item in data ])
    z_min = min([ item.z for item in data ])
# -------------------------------------------------------------------------------------------
# Calculate Maximum of x, y and z co-ordinates
x_max = y_max = z_max = 0
for item in data:
    x_max = max([ item.x for item in data ])
    y_max = max([ item.y for item in data ])
    z_max = max([ item.z for item in data ])
# -------------------------------------------------------------------------------------------