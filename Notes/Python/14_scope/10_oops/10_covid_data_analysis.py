import csv
from collections import defaultdict
# -------------------------------------------------------------------------------------------
with open("covid_data.csv") as f:
    records = [ ]
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        records.append({"country": row[2], "date": row[3], "cases": int(row[5])})
# -------------------------------------------------------------------------------------------
# Total Number of Cases
total = 0
for record in records:
    total += record['cases']
# -------------------------------------------------------------------------------------------
# Total Cases by Country
by_country = defaultdict(int)
for record in records:
    by_country[record['country']] += record['cases']
# -------------------------------------------------------------------------------------------
# Names of all Countries affected by COVID
list_countries = {record['country'] for record in records}
# -------------------------------------------------------------------------------------------
# Total Cases by Country and Date
by_country_date = defaultdict(int)
for record in records:
    by_country_date[(record['country'], record['date'])] += 1
# -------------------------------------------------------------------------------------------
# Countries with less than 10K cases
countries_less_10K = {country: cases for country, cases in by_country.items() if cases < 10000}
# -------------------------------------------------------------------------------------------