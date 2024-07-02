count = int(input())
for _ in range(count):
    H, W, N = map(int, input().split())
    
    # 計算
    floor = N % H
    if floor == 0:
        floor = H
        room = N // H
    else:
        room = N // H + 1
    
    # 結果の出力
    print(f"{floor}{room:02d}")
