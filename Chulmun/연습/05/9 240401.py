# ユーザーに整数を3つ入力してもらう
num1 = int(input("Prease enter the first intger : "))
num2 = int(input("Prease enter the second intger : "))
num3 = int(input("Please enter the third intger : "))

# 3つの整数の最大値を求める
max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max

# 3つの整数のうち、同じ値が2つあったときの値を求める
same_number = None
if (num1 == num2):
    same_number = (num1)
elif (num2 ==num3):
    same_number = (num2)
elif (num1 == num3):
    same_number = (num1)
    

if (num1 != num2 != num3):
    print("All integer is different.The most large integer is",max)
elif (num1 == num2 == num3):
    print("All the numbers are the same.")    
elif ((num1 == num2)or(num2 ==num3)or(num1 == num3)):
    print("The two integer is the same.The integer is",same_number)
