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

