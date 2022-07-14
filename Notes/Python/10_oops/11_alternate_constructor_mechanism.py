class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)
# ------------------------------------------------------------------------------------------        
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @classmethod
    def from_string(cls, string):
        temp = string.split("-")
        return cls(temp[0], temp[1], temp[2])
    
    @classmethod
    def from_json(cls, json_string):
        import json
        data = json.loads(json_string)
        fname = data['name']
        lname = data['lname']
        pay = data['pay']
        return cls(fname, lname, pay)

    def email(self):
        return f'{self.fname}.{self.lname}@company.com'

_json = """
{
    "fname": "steve",
    "lname": "jobs",
    "pay": 1000
}
"""
e = Employee("steve", "jobs", 1000)
e = Employee.from_json(_json)
# ------------------------------------------------------------------------------------------
class Points:
    def __init__(self):
        self._points = [ ]

    @classmethod
    def from_csv(cls):
        p = cls()
        with open('points.txt', 'r') as f:
            for line in f:
                parts = line.split()
                f_parts = list(map(float, parts))
                p._points.append((f_parts[0], f_parts[1], f_parts[2]))
        return p
    
    @property
    def average(self):
        x_total = y_total = z_total = 0
        for item in self._points:
            x_total += item[0]
            y_total += item[1]
            z_total += item[2]
        return (x_total, y_total, z_total)
    
    @property
    def minimum(self):
        x_min = min([ item[0]  for item in self._points ])
        y_min = min([ item[1]  for item in self._points ])
        z_min = min([ item[2]  for item in self._points ])
        return (x_min, y_min, z_min)
    
    @property
    def maximum(self):
        x_max = max([ item[0]  for item in self._points ])
        y_max = max([ item[1]  for item in self._points ])
        z_max = max([ item[2]  for item in self._points ])
        return (x_max, y_max, z_max)
# ------------------------------------------------------------------------------------------