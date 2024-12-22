# 입력 받기
a, b, c = map(int, input().split())

# 리스트로 만든 후, 값을 정렬
dice = [a, b, c]
dice.sort()

# 같은 눈 3개
if dice[0] == dice[1] == dice[2]:
    print(10000 + dice[0] * 1000)
# 같은 눈 2개
elif dice[0] == dice[1] or dice[1] == dice[2]:
    print(1000 + dice[1] * 100)
# 모두 다른 눈
else:
    print(dice[2] * 100)
