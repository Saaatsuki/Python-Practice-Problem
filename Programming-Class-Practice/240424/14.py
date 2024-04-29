import random  # ランダムモジュールをインポート

n = 5  # ランダムに取り出す要素の数
max_num = 6  # ランダムに取り出す要素の最大値

# 1から10までのリストを作成
sample_list = [value for value in range(1, 11)]  


random_list = []  # 空のリストを作成して、ランダムに取り出した要素を格納するためのリスト

for trial_count in range(0, n):  # n回繰り返す
    random_index = random.randint(0, len(sample_list) - 1)  # ランダムなインデックスを生成
    ramdom_num = sample_list.pop(random_index)  # リストからランダムに要素を取り出し、その要素を削除して取り出した値を取得
    random_list.append(ramdom_num)  # 取り出した値をrandom_listに追加
    
print(random_list)  # 結果を表示

# import random: ランダムな数を生成するためのrandomモジュールをインポートします。
# n = 5: ランダムに取り出す要素の数を設定します。
# max_num = 6: ランダムに取り出す要素の最大値を設定します。
# sample_list = [value for value in range(1, 11)]: 1から10までのリストを生成します。
# このリストから要素をランダムに取り出します。
# random_list = []: ランダムに取り出した要素を格納するための空のリストを作成します。
# for trial_count in range(0, n):: n回繰り返します。
# random_index = random.randint(0, len(sample_list) - 1): sample_list内のランダムなインデックスを取得します。
# ramdom_num = sample_list.pop(random_index): ランダムなインデックスの要素を取り出し、その要素をsample_listから削除して、取り出した値をramdom_numに格納します。
# random_list.append(ramdom_num): 取り出した値をrandom_listに追加します。
# print(random_list): 結果を表示します。
# このプログラムは、sample_listからランダムに要素を取り出してrandom_listに格納することをn回繰り返します。取り出した要素は元のリストから削除され、最終的にはrandom_listにランダムな順序で要素が含まれることになります。