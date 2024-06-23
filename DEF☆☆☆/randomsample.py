import random

def getRandomSample1(argSequence, argK):
    # もしシーケンスの長さが抽出する要素の個数より小さい場合、エラーを発生させる
    if len(argSequence) < argK:
        raise ValueError("シーケンスよりも個数が大きいため実行できません")
    
    # 空のリストを準備し、シーケンスのコピーを作成する
    sample_li = []
    argSequence_li = list(argSequence)
    
    # 指定された個数だけ要素を抽出するループ
    for _ in range(argK):
        # ランダムにインデックスを選び、その要素を抽出してsample_liに追加する
        index = random.randint(0, len(argSequence_li) - 1)
        sample_li.append(argSequence_li.pop(index))
    
    # 抽出した要素が入ったリストを返す
    return sample_li


import random

def getRandomSample2(argSequence, argK):
    # もしシーケンスの長さが抽出する要素の個数より小さい場合、エラーを発生させる
    if len(argSequence) < argK:
        raise ValueError("シーケンスよりも個数が大きいため実行できません")   

    # 空のリストを準備し、シーケンスのコピーを作成する
    sample_li = []
    argSequence_li = list(argSequence)

    # 指定された個数だけ重複しない要素を抽出するループ
    while len(sample_li) < argK:
        # ランダムにインデックスを選び、その要素を取得する
        index = random.randint(0, len(argSequence_li) - 1)
        random_sel = argSequence_li[index]

        # もし選ばれた要素がまだsample_liに含まれていなければ、sample_liに追加する
        if random_sel not in sample_li:
            sample_li.append(random_sel)
        
        # 抽出した要素を元のシーケンスから削除する
        argSequence_li.remove(random_sel)

    # 抽出した要素が入ったリストを返す
    return sample_li
