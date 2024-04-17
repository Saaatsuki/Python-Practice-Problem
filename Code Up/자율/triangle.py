def find_side3(side1, side2):
    # 三角形が成立する辺の長さを格納するリストを初期化
    side3 = []

    # 三角形の条件を満たすかどうかをチェック
    for side3 in range(abs(side1 - side2) + 1, side1 + side2):
        side3.append(side3)

    return side3

# 2つの辺の長さを入力
side1 = int(input("1つ目の辺の長さを入力してください："))
side2 = int(input("2つ目の辺の長さを入力してください："))

# 三角形の成立条件を満たす辺の長さを求める
side3 = find_side3(side1, side2)

# 成立する三角形の辺の長さを出力
print("成立する三角形の辺の長さ:", side3)
