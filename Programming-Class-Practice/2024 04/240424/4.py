# 整数の入力を受けて、受けた入力の整数を画面に出力
# 3の倍数か4の倍数だったらプログラミング終了


#やり方①
while True:
    number = int(input("整数を入力してください："))
    if (number%3==0 or number%4==0):
        print("プログラムを終了します")
        break
    else:
        print(number)
        
#やり方②
for count in range(1, 10):
    # countを5で割った余りを出力し、空白で区切って表示
    print(count % 5, end=" ")

    # 入力した整数が3の倍数か4の倍数かを判定
    if count % 3 == 0 or count % 4 == 0:
        # 3の倍数か4の倍数が見つかったのでプログラムを終了
        break