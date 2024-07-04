# テストケースの数を読み込む
T = int(input())

for _ in range(T):
    # 自動車の基本価格を読み込む
    s = int(input())
    # オプションの数を読み込む
    n = int(input())
    
    total_price = s
    
    for _ in range(n):
        q, p = map(int, input().split())
        total_price += q * p
    
    print(total_price)
