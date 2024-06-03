while True:
    number = int(input("整数を入力してください："))
    
    if(number < 0):
        print("負の数です")
    elif(0 < number):
        print("正の数です")
    else:
        break