# ユーザーに土地の面積を平方メートルで入力してもらう
area_meter = float(input("Please enter the area of your land in square meters☆："))

# 平方メートルを平方フィートに変換する関数
def square_meters_to_feet(square_meters):
    square_feet = square_meters * 10.764
    return square_feet

# 平方メートルをエーカーに変換する関数
def square_meters_to_acres(square_meters):
    acres = square_meters / 4046.85642
    return acres

# 入力された値が負の場合、無効な入力としてメッセージを表示する
if (area_meter < 0):
    print("Invalid input")
else:
    # 入力された平方メートルを平方フィートとエーカーに変換し、結果を出力する
    print("The area of this land, in feet, is {} ft², and in acres, it's {} ac".format(square_meters_to_feet(area_meter), square_meters_to_acres(area_meter)))
