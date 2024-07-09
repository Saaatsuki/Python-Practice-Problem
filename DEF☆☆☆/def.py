import random

# in → def getIn()
def getIn(item, container):
    for elem in container:
        if elem == item:
            return True
    return False

# len → def getLen()
def getLen(sequence):
    count = 0
    for _ in sequence:
        count += 1
    return count

# count → def getCount()
def getCount(lst, value):
    count = 0  # カウントの初期化
    # リスト内の各要素を走査
    for item in lst:
        if item == value:  # 要素が指定された値と一致する場合
            count += 1  # カウントを増やす
    return count

# sum → def getSum()
def getSum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# max → def getMax()
def getMax(lst):
    max_value = lst[0]
    for val in lst:
        if val > max_value:
            max_value = val
    return max_value

# all() → def getAll()
def getAll(iterable):
    for elem in iterable:
        if not elem:
            return False
    return True

# pop() → def getPop()
def getPop(lst):
    if not lst:  # リストが空の場合はエラーを出す
        raise IndexError("pop from empty list")

    last_element = lst[-1]  # 最後の要素を取得
    new_lst = []  # 新しいリストを作成

    # 最後の要素以外を新しいリストに追加
    for i in range(len(lst) - 1):
        new_lst.append(lst[i])
    
    # 元のリストをクリアして、新しいリストの要素を元のリストに追加
    while len(lst) > 0:
        lst.remove(lst[0])
    
    for item in new_lst:
        lst.append(item)

    return last_element


# index() → def getIndex()
def getIndex(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1


def sort_list_max_remove(lst):
    sorted_list = []
    while lst:
        max_elem = max(lst)
        sorted_list.append(max_elem)
        lst.remove(max_elem)
    return sorted_list



# テスト用の例
if __name__ == "__main__":
    # getIn() のテスト
    container = [1, 2, 3, 4, 5]
    item = 3
    print(getIn(item, container))  # True

    # getLen() のテスト
    sequence = [1, 2, 3, 4, 5]
    print(getLen(sequence))  # 5

    # getSum() のテスト
    numbers = [1, 2, 3, 4, 5]
    print(getSum(numbers))  # 15

    # getAll() のテスト
    iterable_true = [True, True, True]
    iterable_false = [True, False, True]
    print(getAll(iterable_true))  # True
    print(getAll(iterable_false))  # False

