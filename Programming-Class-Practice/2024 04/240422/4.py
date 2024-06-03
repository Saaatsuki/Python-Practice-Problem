number = int(input("1-100までの整数を入力してください："))

for i in range(1,101):
    if str(number) in str(i):
        print(i)