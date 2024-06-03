numbers = []

for i in range(1,6):
    number = int(input(f"{i}番目の値を入力"))
    numbers.append(number)
    
add = sum(numbers)
ave = add / 5
print(f"結果：{add}")
print(f"平均：{ave}")
