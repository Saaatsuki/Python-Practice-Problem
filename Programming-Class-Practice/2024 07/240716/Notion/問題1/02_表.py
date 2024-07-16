from prettytable import PrettyTable

products = {
    'Apple': 1200,
    'Banana': 800,
    'Cherry': 1500,
    'Date': 600,
    'Elderberry': 900
}

sorted_products = sorted(products.items(),key=lambda x:x[1],reverse=False)
table1 = PrettyTable([" ", "name" ,"value"])
table2 = PrettyTable([" ", "name" ,"value"])

affordable_products = [(name, price) for name, price in sorted_products if price <= 1000]
print(affordable_products)

for idx , (name,val) in enumerate(sorted_products,start=1):
    table1.add_row([idx,name,val])
for idx , (name,val) in enumerate(affordable_products,start=1):
    table2.add_row([idx,name,val])

print(table1)
print(table2)