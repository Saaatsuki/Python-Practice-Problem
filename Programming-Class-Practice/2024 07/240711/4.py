import csv

with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['학교명']}")