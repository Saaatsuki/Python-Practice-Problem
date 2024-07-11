from prettytable import PrettyTable

# data_di = {
#     "name": None,
#     "age": None,
#     "city": None
# }

data_li = []

while True:
    name = input("\n이름은 입력 : ")
    if name == "1":
        break
    age = int(input("나이를 입력 : "))
    city = input("출신 도시를 입력 : ")

    data_di = {
    "name": name,
    "age": age,
    "city": city
    }
    data_li.append(data_di)

table = PrettyTable()
table.field_names = ["name" ,"age" , "city"]
for dic in data_li: 
    table.add_row([dic["name"], dic["age"], dic["city"]])
print(table)

# print()
# print()
# for key in person_di_1:
#     print(f"Key : {key} , Value : {person_di_1[key]}")

# print()
# for key , value in person_di_1.items():
#     print(f"Key : {key} , Value : {value}")

# print()
# for key in person_di_1.keys():
#     print(f"Key : {key}")

# print()
# for value in person_di_1.values():
#     print(f"Value : {value}")

# print()
# table = PrettyTable()
# table.field_names = ["name" ,"age" , "city"]
# for dic in data_li: 
#     table.add_row([dic["name"], dic["age"], dic["city"]])
# print(table)