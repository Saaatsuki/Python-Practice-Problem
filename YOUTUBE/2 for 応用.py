last_names = ["大野","櫻井","相葉","二宮","松本"]
first_names = ["智","翔","雅紀","和也","潤"]

print(last_names[0]+first_names[0])
print(last_names[1]+first_names[1])
print(last_names[2]+first_names[2])
print(last_names[3]+first_names[3])
print(last_names[4]+first_names[4])

for name in range(len(last_names)):
    print(last_names[name] + first_names[name])
    
# 複数の場合はrangeじゃなくてzip
for last_name,first_name in zip(last_names,first_names):
    print(last_name+ first_name)
    
print("出席番号",0,"番目の"+last_names[0])
print("出席番号",1,"番目の"+last_names[1])
print("出席番号",2,"番目の"+last_names[2])
print("出席番号",3,"番目の"+last_names[3])
print("出席番号",4,"番目の"+last_names[4])

for i in range (len(last_names)):
    print("出席番号",i,"番目の"+last_names[i])
    
for number,last_name in enumerate(last_names): #enumerate()でリストの要素と要素番号を同時に取得
    print("出席番号",number,"番目の"+last_name)