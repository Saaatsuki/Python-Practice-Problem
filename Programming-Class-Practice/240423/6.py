print("-------------------------")
print("1，奇数と偶数の区分プログラム")
print("2，3の倍数　確認プログラム")
print("-------------------------")

menu = int(input("メニューを選択してください(1 or 2)\n"))

if (menu == 1):
    print("奇数と偶数を区別するプログラムを始めます")
    number = int(input("整数の値を入力してください\n"))
    if (number % 2 == 0):
        print("入力した値", number, "は偶数です")
    else:
        print("入力した値", number, "は奇数です")

        
elif (menu == 2):
    print("3の倍数の確認プログラムを始めます")
    number = int(input("整数の値を入力してください\n"))
    if (number % 3 == 0):
        print("入力した値", number, "は3の倍数です")
    elif(number % 3 != 0):
        print("入力した値", number, "は3の倍数ではありません")
    elif (number == 3):
        print("入力された値は3です")

else:
    print("1か2を選択してください")
