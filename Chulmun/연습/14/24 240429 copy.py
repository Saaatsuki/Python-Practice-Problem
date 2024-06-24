numbers_str = map(int, input("숫자들을 쉼표로 구분하여 입력하세요 : ").split(','))

# リスト内包表記を使って数値のリストを作成する
numbers = [num for num in numbers_str]

result = 0
for num in numbers:
    result += num

if (result <= 100):
    print("총합이 100을 초과하지 않습니다.\n입력된 모든 숫자 : ", numbers, "\n최종 총합 : ", result)
else:
    print("총합이 100을 초과합니다.\n현재까지 입력된 값들 : ", numbers, "\n현재까지의 총합 : ", result)

