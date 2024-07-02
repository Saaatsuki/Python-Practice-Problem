N = int(input())  # 整数の数Nを入力

# 整数を空白で区切ってリストに格納
numbers = list(map(int, input().split()))

# 探す整数vを入力
v = int(input())

# numbersリスト内でvが何個かを数えて出力
count_v = numbers.count(v)

# for num in numbers:
#     if num == v:
#         count_v += 1

print(count_v)

