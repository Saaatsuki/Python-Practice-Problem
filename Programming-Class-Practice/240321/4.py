# ユーザーからの距離をkm単位で入力してもらう
distance = input("光が旅する距離をkmで入力してね☆：")

# 入力した距離を小数にする
distance = float(distance)
# distance = float(input("光が旅する距離をkmで入力してね☆："))でも可能

spead = 299792 # 光の速度

time = distance / spead

print("光が", distance , "km 旅するのにかかった時間は約", time ,"秒です。")





