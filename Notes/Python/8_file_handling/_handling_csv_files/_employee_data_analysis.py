import csv
from collections import defaultdict

with open('data/employees.csv') as f:
    records = []
    rows = csv.reader(f)
    headers = next(rows)    # Skipping Headers
    for row in rows:
        records.append({"name": row[0], "gender": row[1], "team": row[2], "pay": row[3]})

# Total Pay to all employees
total = 0.00
for record in records:
    total += float(record['pay'])

salary = sum([float(record['pay']) for record in records])

# Want to Know total number of Male and Female employees
gender_count = {}

for record in records:
    if record['gender'] in gender_count:
        gender_count[record['gender']] += 1
    else:
        gender_count[record['gender']] = 1

# Using defaultdict
gender_count = defaultdict(int)

for record in records:
    gender_count[record['gender']] += 1

# Sort Employee records based in name
sorted_names = sorted(records, key=lambda item: item['name'])

for item in sorted_names:
    print(item)

# Sort Employee records based on pay
sorted_pay = sorted(records, key=lambda item: float(item['pay']))

# How many unique teams are present
unique_teams = {record['team'] for record in records}

# List Comprehension
teams = [record['team'] for record in records]
print(set(teams))

# Names of those employees who are taking more than 80K per month.
more_80 = {record['name']: record['pay'] for record in records if float(record['pay']) >= 80000}
print(sorted(more_80.items(), key=lambda item: item[-1]))
