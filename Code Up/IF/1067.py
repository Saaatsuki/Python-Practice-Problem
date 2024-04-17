# 整数を入力します
num = int(input("整数を入力してネ："))

# 負数か正数かを判別し、結果を出力します
if num < 0:
    print("minus")
else:
    print("plus")

# 奇数か偶数かを判別し、結果を出力します
if num % 2 == 0:
    print("even")
else:
    print("odd")