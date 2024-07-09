data = [
    ["Name", "Age", "City"],
    ["Alice", "24", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "22", "Chicago"]
]

for row in data:
    print("{:<10} {:<10} {:<15}".format(*row))
