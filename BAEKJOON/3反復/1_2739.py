while True:
    number = int(input("九九の段を入力してください（1-9の間）："))
    if 1 <= number <= 9:
        for i in range(1, 10):
            print(number, "X", i, "=", number * i)
        break
    else:
        print("1から9の値を入力してください。")
