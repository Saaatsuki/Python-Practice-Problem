# addThreeNumbers を3回呼び出し、
# それぞれの呼び出しで異なる3つの数字を使って合計を計算する

def addThreeNumbers(num1, num2, num3):
    totalsum = num1 + num2 + num3
    return totalsum

# 最初の呼び出し: 1, 2, 3を使って合計を計算
sum1 = addThreeNumbers(1, 2, 3)

# 2番目の呼び出し: 3, 4, 5を使って合計を計算
sum2 = addThreeNumbers(3, 4, 5)

# 3番目の呼び出し: 10, 11, 12を使って合計を計算
sum3 = addThreeNumbers(10, 11, 12)
