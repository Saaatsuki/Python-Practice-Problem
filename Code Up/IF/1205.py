a, b = map(float, input("Please enter two real numbers separated by a space: ").split())

# 加算、減算、乗算、除算、二乗の結果をリストに格納
results = [a + b, a - b, b - a, a * b, a / b, b / a, a ** b, b ** a]

# 結果の最大値を計算し、小数点以下6桁で出力
max_result = max(results)
print("{:.6f}".format(max_result))
