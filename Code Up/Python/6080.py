# 入力から2つのサイコロの目の数を読み込む
diceA, diceB = map(int, input().split())

# diceAの目の範囲（1からdiceAまで）をループする
for i in range(1, diceA+1):
    # diceBの目の範囲（1からdiceBまで）をループする
    for j in range(1, diceB+1):
        # サイコロAとサイコロBの出目の組み合わせを出力する
        print(i, j)