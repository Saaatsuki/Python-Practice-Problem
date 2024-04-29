# ユーザーから温度を入力
temperature = int(input("Prease enter a temperature : "))

# 温度に応じて推奨されるアクティビティを決定する関数
def temperture_recommand ():
    
    global temperature

    if (30 <= temperature):
        return("swimming🐡")
    elif (20 <= temperature <30):
        return("hiking🏔")
    elif (10 <= temperature < 20):
        return("cycling🚴")
    else:
        return("ski🎿")

# 推奨されるアクティビティを取得＆出力
recommendation = temperture_recommand()
print("Recommended activity:", recommendation)