# num1 , num2 , num3 = map(int,input().split())
def count_visits(N, r, c):
    # 2^N x 2^Nの配列の探索順序を計算する関数
    def visit_count(x, y, size, r, c):
        if size == 1:
            return 0
        
        half_size = size // 2
        if r < x + half_size and c < y + half_size:
            # 左上
            return visit_count(x, y, half_size, r, c)
        elif r < x + half_size and c >= y + half_size:
            # 右上
            return visit_count(x, y + half_size, half_size, r, c) + half_size * half_size
        elif r >= x + half_size and c < y + half_size:
            # 左下
            return visit_count(x + half_size, y, half_size, r, c) + 2 * half_size * half_size
        else:
            # 右下
            return visit_count(x + half_size, y + half_size, half_size, r, c) + 3 * half_size * half_size
    
    size = 2 ** N
    return visit_count(0, 0, size, r, c)

# 入力の読み込み
N, r, c = map(int, input().split())

# 結果の出力
print(count_visits(N, r, c))
