#18)
list18 = ["Hello","World","Cheol"]    
found_word = False  

for i in list18:
    if i.upper() == "WORLD":
        print("単語を見つけました")
        found_word = True
if not found_word :
    print("単語を見つけることができませんでした。ぴえん")

    
for i in list18:
    if i.upper() == "WORLD":
        print("単語を見つけました")
        break
else:
    print("単語を見つけることができませんでした。ぴえん")
    