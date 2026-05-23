import csv
with open("..\Data\data.csv") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['Name'], row['Country'])
print(type(row))