numbers = []  # 入力された数値を格納するリストを初期化

for i in range(1, 3):
    number = int(input(f"{i}번째의 정수를 입력 해주세요: "))
    numbers.append(number)  # 入力された数値をリストに追加

result = 1
for num in numbers:
    result *= num  # リスト内の数値を掛け合わせて結果を計算

print(result)
