employees = {
    'John': 28,
    'Paul': 35,
    'George': 33,
    'Ringo': 40,
    'Mick': 29
}

sorted_employees = sorted(employees.items() , key=lambda x:x[1],reverse=True)
sorted_employees_30 = [(name,age) for name,age in sorted_employees if 30<=age]

for name , age in sorted_employees_30:
    print(f"{name} : {age}")