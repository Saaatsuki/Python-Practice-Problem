import random

def custom_pop(lst):
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

# テスト
my_list = [1, 2, 3, 4, 5]
print(custom_pop(my_list))  # 5
print(my_list)  # [1, 2, 3, 4]


def randomSample(argSequence,argK):
    sample = []
    argSequence_copy = argSequence
    for _ in range(argK):
        index = random.randint(0,len(argSequence_copy-1))
        sample.append(argSequence_copy.pop(index))
    return sample