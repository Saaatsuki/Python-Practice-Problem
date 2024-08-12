# # ユークリッドの互除法を使って最大公約数を求める関数
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # 最小公倍数を求める関数
# def lcm(a, b):
#     return a * b // gcd(a, b)

# # リスト内の数値の最大公約数を求める関数
# def gcd_of_list(numbers):
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = gcd(result, num)
#     return result

# # リスト内の数値の最小公倍数を求める関数
# def lcm_of_list(numbers):
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = lcm(result, num)
#     return result


while True:
    num1 , num2 = map(int,input().split())

    if num1 == 0 and num2 == 0:
        break
    else:
        if num2 % num1 == 0:
            print("factor")
        elif num1 % num2 == 0:
            print("multiple")
        else:
            print("neither")