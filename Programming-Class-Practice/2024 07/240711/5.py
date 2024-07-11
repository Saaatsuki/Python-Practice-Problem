from prettytable import PrettyTable

person_di = {
    "name" : "Kawai",
    "age" : 24 ,
    "city" : "New York"
}

print()
print()
for key in person_di:
    print(f"Key : {key} , Value : {person_di[key]}")

print()
for key , value in person_di.items():
    print(f"Key : {key} , Value : {value}")

print()
for key in person_di.keys():
    print(f"Key : {key}")

print()
for value in person_di.values():
    print(f"Value : {value}")

print()
table = PrettyTable()
table.field_names = ["name" ,"age" , "city"]
table.add_row([
    person_di["name"] , f'{person_di["age"]} 명' , person_di["city"]
])
print(table)