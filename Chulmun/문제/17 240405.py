resident_number = input("Please enter your resident number : ")


# 住民番号の有効性を検証する関数
def validate_resident_number(resident_number):
     # 住民番号が13桁の数字でない場合は無効
    if len(resident_number) != 13 or not resident_number.isdigit:
        return False
    
    # 住民番号の最後の桁を検証番号として取得
    check_degit = int(resident_number[-1])
    # 重みを定義
    weight = [2,3,4,5,6,7,8,9,2,3,4,5]
    # 重みを適用し、住民番号の前12桁の合計を計算
    total = sum(int(resident_number[i])*weight[i] for i in range(12))
    # 合計を11で割って余りを計算
    remainder = total%11
    # 11から余りを引いて検証番号を計算
    result = 11 - remainder if remainder != 0 else 0
    # 結果が2桁の場合、10の位を削除して1桁のみを使用
    result = result % 10
    
    # 計算された検証番号と入力された検証番号が一致するかどうかを検証
    return result == check_degit



if validate_resident_number(resident_number):
    print("This is a valid resident number")
else:
    print("This is a invalid resident number")