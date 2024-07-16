from prettytable import PrettyTable

students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 90,
    'Eva': 95
}

students_sorted = sorted(students.items() , key= lambda x:x[1] , reverse=True)

top3 = students_sorted[:3]

table = PrettyTable(["name","score"])

for name , score in top3:
    table.add_row([name , score])

print(table)