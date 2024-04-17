# ユーザーにアルファベットの文字を入力してもらう
a = input()

# アルファベットの最初の文字 'a' のUnicodeコードポイントを取得して、startに代入する
start = ord('a')

# 無限ループを開始する
while True:
    # chr(start)を使って、Unicodeコードポイントを文字に変換して出力する
    print(chr(start), end=' ')
    
    # もし表示した文字がユーザーが入力した文字aと等しい場合、ループを終了する
    if (chr(start) == a):
        break
    
    # startの値を1つ増やして、次の文字を表示する準備をする
    start = start + 1
