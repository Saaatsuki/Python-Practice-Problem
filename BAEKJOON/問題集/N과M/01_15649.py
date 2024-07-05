def DFS():
    # 現在の数列sの長さがMと等しい場合、出力して終了する
    if len(s) == M:
        print(*s)  # リストsの要素をスペースで区切って出力
        return

    # 1からNまでの数字について順にチェックする
    for i in range(1, N + 1):
        # もしiが既に数列sに含まれている場合はスキップする
        if i in s:
            continue

        # 数列sにiを追加する
        s.append(i)
        # DFS関数を再帰的に呼び出し、次の数字を追加する
        DFS()
        # 追加したiをsから取り除き、元の状態に戻す
        s.pop()


# 標準入力からNとMを読み込み、整数に変換する
N, M = map(int, input().split())
s = []  # 数列を保持するための空のリスト
DFS()  # DFS関数を呼び出して探索を開始する