def getIn(argSequence, argCheck):
    for val in argSequence:
        if val == argCheck:
            return True
    return False

def getSum(argList):
    total = 0
    for val in argList:
        total += val
    return total

def getArg(argList):
    return getSum(argList) // len(argList)

def getMax(argList):
    max_val = argList[0]
    for val in argList:
        if val > max_val:
            max_val = val
    return max_val

def getSet(argList):
    set_li = []
    for val in argList:
        if not getIn(set_li, val):  
            set_li.append(val)
    return set_li

def getCount(argList,argCheck):
    count = 0
    for val in argList:
        if val == argCheck:
            count+=1
    return count

# 整数の数をユーザーに入力してもらう
num_count = int(input("いくつの整数を入力しますか？（最低3つ）: "))

# 最低3つの整数を入力するように促す
while num_count < 3:
    num_count = int(input("最低でも3つの整数を入力してください："))

# 整数をリストに格納する
numbers = []
for i in range(num_count):
    num = int(input(f"{i + 1}番目の整数を入力してください: "))
    numbers.append(num)

# 与えられた整数の関係に応じてメッセージを出力する
if all(num == numbers[0] for num in numbers):
    print("すべての数が同じです。")
elif any(getCount(numbers,num) >= 2 for num in numbers):
    duplicates = getSet(num for num in numbers if numbers.count(num) >= 2)
    print(f"少なくとも2つの数が同じです。({', '.join(map(str, duplicates))})")
else:
    max_num = getMax(numbers)
    print(f"すべての数が異なります。最大の数は {max_num} です。")

