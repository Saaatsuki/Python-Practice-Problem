# 異なる余りを格納するリストを初期化します
remainders = []

# 10回のループで数を入力し、それぞれの剰余を求めます
for _ in range(10):
    number = int(input())  # 入力から数を取得します
    remainder = number % 42  # 数を42で割った余りを計算します
    # もし現在の剰余がリストにない場合、追加します
    if remainder not in remainders:
        remainders.append(remainder)

# 異なる剰余の数を出力します
print(len(remainders))
