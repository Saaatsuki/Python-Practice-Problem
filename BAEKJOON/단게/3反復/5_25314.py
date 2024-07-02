N = int(input())

# Nが4の倍数であるかを確認し、適切な整数データ型を選択する
if N % 4 == 0:
    data_type = "long int"
else:
    # 4で割り切れない場合、余りを計算し、適切な数のlong intを選択する
    remainder = N % 4
    num_longs = (N // 4) + 1
    data_type = "long int" * num_longs

print(data_type)
