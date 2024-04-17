# グローバル変数 count の値を1で初期化します。
count = 1

# カウントを増やす関数を定義します。
def incrementCount():
    # global キーワードを使用して、関数内でグローバル変数 count を使用することを宣言します。
    global count
    # count の値を1増やします。
    count += 1  # count = count + 1 の短縮形

# カウントを減らす関数を定義します。
def decrementCount():
    # global キーワードを使用して、関数内でグローバル変数 count を使用することを宣言します。
    global count
    # count の値を1減らします。
    count -= 1  # count = count - 1 の短縮形

# incrementCount 関数を呼び出して、count の値を増やします。

incrementCount()
# count の値を出力します。
print(count)

# decrementCount 関数を呼び出して、count の値を減らします。
decrementCount()
# count の値を出力します。
print(count)
