import csv

with open('grade.csv' , 'r' , newline='' , encoding='urf-8') as f_handler:
    reader = csv.reader(f_handler)
    header = next(reader)


    for row in reader:
        print(row)
