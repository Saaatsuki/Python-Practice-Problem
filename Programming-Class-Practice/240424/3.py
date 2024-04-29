# 入力した値が奇数なら3の倍数を出力せよ

number = int(input("整数を入力してください："))

if (number%2!=0):
    if (number%3==0):
        print(number)