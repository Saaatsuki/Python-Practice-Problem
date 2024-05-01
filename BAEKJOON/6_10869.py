numbers = []
for i in range(1, 3):
    number = int(input(f"{i}番目の整数を入力してください："))
    numbers.append(number)
    
while numbers[1] == 0:
    print("エラー：2番目の整数には0以外の値を入力してください。")
    numbers[1] = int(input("再度2番目の整数を入力してください："))



res1 = numbers[0] + numbers[1]
res2 = numbers[0] - numbers[1]
res3 = numbers[0] * numbers[1]
res4 = numbers[0] / numbers[1]
print("加算結果：", res1)
print("減算結果：", res2)
print("乗算結果：", res3)
print("除算結果：", res4)