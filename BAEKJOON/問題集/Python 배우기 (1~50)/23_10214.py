T = int(input())

for _ in range(T):
    score_y = 0
    score_k = 0
    for _ in range(9):
        num1 , num2 = map(int,input().split())
        score_y += num1
        score_k += num2

    if score_y < score_k:
        print("Korea")
    elif score_k < score_y:
        print("Yonsei")
    else:
        print("Draw")