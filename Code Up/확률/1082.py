def hex_multiplier(hex_digit):
    # 16進数を10進数に変換
    decimal_value = int(hex_digit, 16)
    
    # 出力文字列を初期化
    output = ""
    
    # 1からFまでの各数値を乗算して結果を出力文字列に追加
    for i in range(1, 16+1):
        # 乗算結果を16進数で出力
        output += f"{hex_digit}*{hex(i)[2:].upper()}={hex(decimal_value * i)[2:].upper()} "
    
    # 結果を返す
    return output

# 入力を受け取る
hex_digit = input()

# 結果を出力
print(hex_multiplier(hex_digit))