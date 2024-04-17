number = (int(input("Please enter the number which is the automatic compression criteria for the trash can : ")))

# 10の位と1の位を入れ替え、2をかける
reverse_number = (number%10)*10 + (number//10)*2


# 結果が100を超える場合、100の位を無視する
if (reverse_number >= 100):
    reverse_number%=100
    
print(reverse_number)

# 結果が50以下かどうかを判定し、結果に応じて出力する
if (reverse_number <= 50):
    print("GOOOOOOOOOOD")
else:
    print("Oh MY GOOOOOOOOOOD")