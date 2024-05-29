model = input("사용자는 모델을 빨리 입력해!!! : ").upper()

maker = ""

#1)
if model == "M3" or model == "M5" or model == "M7":
    maker = "BMW"
elif model == "X" or model == "Y":
    maker = "Tesla"
elif model == "G80" or model == "G90":
    maker = "Hyunday"
else:
    print("알 수 없는 모델입니다.")
    
    
#2) 
list_bmw = []
for i in range(9):
    bmw = f"M{i+1}"
    list_bmw.append(bmw)
list_tesla = ["Y","X"]
list_lexus = ["ES","LS"]
list_genesis = ["G80","G90"]

if model in list_bmw:
    maker = "BMW"
elif model in list_tesla:
    maker = "Tesla"
elif model in list_lexus:
    maker = "lexus"
elif model in list_genesis:
    maker = "Genesis"
else:
    maker = "알 수 없는 모델입니다."
    
print(maker)

#3)
for i in list_bmw:
    if model == i:
        maker = "BMW" 
        break
                  
if maker == "":      
    for i in list_tesla:
        if model == i:
            maker = "Tesla"
            break
            
if maker == "":            
    for i in list_lexus:
        if model == i:
            maker = "Lexus"
            break
            
if maker == "":            
    for i in list_genesis:
        if model == i :
            maker = "Genesis"
            break

if maker =="":
    maker = "알 수 없는 모델입니다."
            

    
print(maker)



list_model = [list_bmw, list_tesla, list_lexus, list_genesis]

# 회사별 자동차 덕록을 가지고 온다. 반복 -> 4회 -> bmw, tesla, lexus, genesis
# 세로 반복
for maker_list in list_model:
    for model_in_list in maker_list:
        if model == model_in_list:
                print("make の値はありません")