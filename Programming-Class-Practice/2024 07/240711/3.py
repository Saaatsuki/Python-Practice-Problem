import csv 

with open('grade.csv' , newline='' , encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f'{row["이름"]} , {row["총점"]} , {row["평균"]}')