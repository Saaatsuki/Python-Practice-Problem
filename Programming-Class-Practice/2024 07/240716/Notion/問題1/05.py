from prettytable import PrettyTable

schools = {
    'School A': 450,
    'School B': 700,
    'School C': 300,
    'School D': 600,
    'School E': 750
}

sorted_schools = sorted(schools.items(),key=lambda x:x[1],reverse=True)
top3 = sorted_schools[:3]

table = PrettyTable([" ","SCHOOL","PEOPLE"])

for i , (school,people) in enumerate(top3,start=1):
    table.add_row([i,school,f"{people} 명"])

print(table)