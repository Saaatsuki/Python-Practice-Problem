from prettytable import PrettyTable

cities = {
    'Tokyo': 13929286,
    'Osaka': 2691189,
    'Nagoya': 2295639,
    'Fukuoka': 1549527,
    'Sapporo': 1952356
}

sorted_cities = sorted(cities.items(),key=lambda x:x[1],reverse=False)
sorted_cities_10man = [(city,people) for city,people in sorted_cities if people<=1000000]

table = PrettyTable([" ","city","people"])

for i ,(city,people) in enumerate(sorted_cities,start=1):
    table.add_row([i,city,f"{people:,} 명"])

print(table)