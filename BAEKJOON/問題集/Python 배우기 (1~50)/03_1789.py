def getMax(argNum):
    N = 0
    total = 0
    while total<=argNum:
        N += 1
        total += N
    return N - 1


S = int(input())
print(getMax(S))

'''実行例の解説
例えば、
𝑆
=
200
S=200 の場合：

初期状態：

N = 0
total = 0
1回目のループ：

N = 1
total = 1 （0 + 1）
2回目のループ：

N = 2
total = 3 （1 + 2）
3回目のループ：

N = 3
total = 6 （3 + 3）
...

19回目のループ：

N = 19
total = 190 （171 + 19）
20回目のループ：

N = 20
total = 210 （190 + 20）
ここで、total が 200 を超えたためループが終了します。そのため、N - 1 の値、すなわち 19 を返します。

このようにして、連続する自然数の合計が指定された数を超えない最大の N を求めることができます。'''