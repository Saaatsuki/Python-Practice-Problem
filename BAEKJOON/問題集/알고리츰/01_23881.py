# 入力を読み込む
n, exchange = map(int, input().split())  # n: 配列のサイズ, exchange: 交換回数K
arr = list(map(int, input().split()))  # 配列の要素を読み込む
index = 0  # 最大値のインデックスを保持する変数
swap = 0  # 交換回数をカウントする変数

# 選択ソートを実行する（逆順）
for i in range(n-1, 0, -1):  # 配列の最後から先頭に向かってループ
    index = i  # 初期値として現在のインデックスを最大値のインデックスとする

    # 部分配列 arr[0..i] の中で最大値のインデックスを探す
    for j in range(0, i+1):  # jを0から始める
        if arr[j] > arr[index]:  # 最大値のインデックスを更新
            index = j

    # 最大値が現在の位置 i と異なる場合に交換を行う
    if i != index:
        arr[i], arr[index] = arr[index], arr[i]  # 交換を実行
        swap += 1  # 交換回数をインクリメント

        # 交換回数が指定された回数に達した場合、結果を出力して終了
        if swap == exchange:
            print(min(arr[index], arr[i]), max(arr[index], arr[i]))  # 交換された2つの要素を小さい順に出力
            exit()  # プログラムを終了

# もし交換回数が指定された回数に達しなかった場合 -1 を出力
print(-1)
