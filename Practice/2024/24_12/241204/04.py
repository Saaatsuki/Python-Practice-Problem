# この関数は2つの整数を受け取り、その合計と平均を計算し、
# それらをリストに格納して返します。
def get_sum_avg(argA, argB):
    # 合計と平均を計算
    sum_value = argA + argB
    avg_value = sum_value // 2  # 整数の平均を計算

    # 合計と平均を格納するリストを作成
    ret_value = [sum_value, avg_value]

    # 合計と平均を含むリストを返す
    return ret_value

# get_sum_avg関数をテストするためのメイン関数
if __name__ == "__main__":
    # get_sum_avg関数を2と6の値で呼び出し
    bar = get_sum_avg(2, 6)

    # 合計と平均を表示
    print("Sum:", bar[0])  # bar[0]は合計
    print("Average:", bar[1])  # bar[1]は平均
