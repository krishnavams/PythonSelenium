import csv
from collections import defaultdict

# Reading CSV Files
with open('portfolio.csv', 'r') as csv_file:
    rows = csv.reader(csv_file)  # rows is an iterator object
    for row in rows:  # Each row is represented as a Python list
        print(row)     # Prints each line of csv file.

with open('portfolio.csv', 'r') as csv_file:
    rows = csv.reader(csv_file)
    for row in rows:
        print(row[0], row[1])     # Prints only first and second column.

# Uisng DictReader
with open('portfolio.csv', 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    for row in rows: # Each row is represented as a Python dictionary
        print(row['name'], row['shares'])

# Writing to CSV Files
with open('new_portfolio.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'shares', 'price'])

# Using DictWriter
with open('portfolio.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, ['name', 'shares', 'price'])
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'IBM', 'shares': 100, 'price': 65.3})


data = [('apple', 'google', 'yahoo'), ('microsoft', 'netflix', 'gmail')]
with open('company.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)  # Write rows takes a list of iterables

# Reading CSV rows as columns
cols = defaultdict(list)

def read_columns(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for header, r in zip(headers, row):
                cols[header].append(r)
    return cols

print(read_columns('portfolio.csv'))