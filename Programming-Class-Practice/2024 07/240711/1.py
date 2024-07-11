import csv

with open('output.csv',mode='w',newline='',encoding='usf-8') as f:
    fields = ['Name' , 'Age' , 'Email']

    writer = csv.DictWriter(f , fieldnames=fields)

    writer.writeheader()

    writer.writerow({'Name' : 'Alice' , 'Age' : 30 , 'Email' : 'alice@example.com'})
    writer.writerow({'Name' : 'Bob' , 'Age' : 30 , 'Email' : 'bob@example.com'})