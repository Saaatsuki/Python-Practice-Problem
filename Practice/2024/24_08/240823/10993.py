N = int(input())

# 위쪽 부분 (N개의 줄)
for i in range(N):
    # 왼쪽 공백 부분
    print(" " * i, end="")
    
    # 별 출력
    for j in range(2 * (N - i) - 1):
        if j % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()

# 아래쪽 부분 (N-1개의 줄)
for i in range(N - 1):
    # 왼쪽 공백 부분
    print(" " * (N - 2 - i), end="")
    
    # 별 출력
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()
