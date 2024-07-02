'''
この問題は、チェス盤のように白と黒が交互に配置された8x8の正方形を、大きなM×Nサイズのボードから切り出すために、最小の再塗装数を計算する問題です。以下は問題の詳細な解説です。

### 問題の概要
1. **入力**：
   - 最初の行に、ボードの行数 `N` と列数 `M` が与えられます（8 ≦ N, M ≦ 50）。
   - 次の `N` 行には、各行のボードの状態が文字列で与えられます。'B' は黒、'W' は白を表します。

2. **出力**：
   - 8x8のチェス盤に再塗装するために必要な最小の塗り替え回数を出力します。

### チェス盤の規則
チェス盤は、以下の2つのパターンのどちらかで構成されます：
- パターン1: 左上が白（'W'）から始まるチェス盤
  ```
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  ```
- パターン2: 左上が黒（'B'）から始まるチェス盤
  ```
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  BWBWBWBW
  WBWBWBWB
  ```

### 解法のステップ
1. **部分ボードの抽出**：
   - 8x8の部分ボードを、N行M列のボードの全ての位置から抽出します。

2. **塗り替えのカウント**：
   - 各8x8の部分ボードに対して、上記の2つのパターンに一致させるために必要な塗り替え回数を計算します。

3. **最小値の特定**：
   - 全ての8x8部分ボードに対して計算した塗り替え回数の最小値を求めます。

### 実装例

```python
# 入力を受け取る
N, M = map(int, input().split())
original = [input() for _ in range(N)]
count = []

# 各8x8部分ボードに対して計算する
for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

# 最小の塗り替え回数を出力する
print(min(count))
```

### 詳細説明
1. **入力の処理**：
   - `N` と `M` を読み込みます。
   - ボードの状態を `original` リストに格納します。

2. **部分ボードの走査**：
   - ボードの全ての位置から8x8の部分ボードを抽出します。
   - 各部分ボードに対して、チェス盤の2つのパターンとの一致を確認します。

3. **塗り替え回数の計算**：
   - 部分ボードの各マスをチェックし、チェス盤パターン1と一致しない場合に `index1` をインクリメントします。
   - 同様に、チェス盤パターン2と一致しない場合に `index2` をインクリメントします。
   - `index1` と `index2` の小さい方を `count` リストに追加します。

4. **最小値の出力**：
   - `count` リストの中の最小値を出力します。

このアプローチにより、ボードの全ての8x8部分ボードに対して最小の塗り替え回数を効率的に計算できます。
'''
# 入力を受け取る
N, M = map(int, input().split())
original = [input() for _ in range(N)]
count = []

# 各8x8部分ボードに対して計算する
for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

# 最小の塗り替え回数を出力する
print(min(count))
