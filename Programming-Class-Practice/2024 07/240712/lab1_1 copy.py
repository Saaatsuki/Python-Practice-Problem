import csv

with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    se = set() 
    for row in reader:
        se.add(row['시도교육청'])

    for idx , val in enumerate(se):
        print(f"{(idx+1):2d} 번 : {val}")
