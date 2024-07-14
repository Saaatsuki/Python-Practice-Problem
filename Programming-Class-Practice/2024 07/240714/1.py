fruits = {'apple': 10, 'banana': 5, 'cherry': 7}

# keys()
print(fruits.keys())

print()
for key in fruits.keys():
    print(key)

print()
print(list(fruits.keys()))

print()
print(" 💙 ".join(fruits.keys()))


# values()
print(fruits.values())

print()
for val in fruits.values():
    print(val)

# items()
print()
for item in fruits.items():
    print(item)

for key , val in fruits.items():
    print(f"{key}は{val}個、在庫あります💙")

fruits_li = [f"{key} 💙 {val}" for key , val in fruits.items()]
print(fruits_li)