names = ["大野","櫻井","相場","二宮","松本"]

print(names[0],"さん")
print(names[1],"さん")
print(names[2],"さん")
print(names[3],"さん")
print(names[4],"さん")


for i in range(len(names)):
    print(names[i]+" さん")
    
for number in range (20):
    print(number+1)

sum = 0
for number in range(20):
    sum = sum + (number+1)   # sum =+ (number+1)
    print(sum)
    
    for name in names:  #リストは複数形にするとわかりやすい！！[names]というリストからnameを取り出す
        print(name + "さん")
        