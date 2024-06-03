# カスタムの 'in' 演算子を定義する関数
def myInOperator(argV, argSeq):
    pass  # この関数では何も行われません

# 文字列の中に指定された文字が含まれているかをチェック
print("a" in "abc")  # => True ('a' は 'abc' に含まれている)

# リストに指定された値が含まれているかをチェック
bar = [1, 2, 3]
print(4 in bar)       # => False (4 は bar に含まれていない)
print(4 not in bar)   # => True (4 は bar に含まれていない)

# カスタム 'in' 演算子を使用して関数を呼び出す
# この関数は何も行わず、単に pass ステートメントで終了する
print(myInOperator(3, [2, 3, 4]))  # => None (関数は何も返さない)


