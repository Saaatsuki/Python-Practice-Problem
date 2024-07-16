from prettytable import PrettyTable

employees = {
    'John': 28,
    'Paul': 35,
    'George': 33,
    'Ringo': 40,
    'Mick': 29
}

sorted_employees = sorted(employees.items(),key=lambda x:x[1],reverse=True)

table = PrettyTable([" ","name","age"])

for idx , (name,age) in enumerate(sorted_employees,start=1):
    table.add_row([idx,name,age])

print(table)