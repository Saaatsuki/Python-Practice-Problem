#1)
for _ in range(10):
    print(1)
    
#2)    
count = 0
while count < 10:
    count += 1
    print(2)
    
#3)
for value in range(7,8):
    print(value)

#4)
for value in range(7,-8): #range(7,8,1)
    print(value)

#5)
for value in range(7,-8,-1):
    print(value)
    
#6)
for value in range(6,5,-2):
    print(value)
    
#7)
for i in range(5,-20,-5):
    print(i)
     
#8)
for i in range(5,-21,-5):
     print(i)
     
#9)
for _ in range(9):
    print(_,end="")
print("\n","*"*20)
print("\n","*"*20,sep="")

for dan in range(2,10):
    print(dan,end="")
    print()


#10)1から20までのリスト
list10 =[]
for num in range(1,21):
    list10.append(num)
print(list10)

list10 = [num for num in range(1, 21)]
print(list10)          


#11)
# #value = int(input("양의 정수를 입력해!!! : "))
# list11 = [value for value in range(1,value)]
# print(list11)

#12)7を100個格納しているリスト 
num = 7
list12 = [num for _ in range(100)]
print(list12)

list12_2 = []
for _ in range(100):
    list12.append(7)
    
list12_3 = [7] * 100


#13)
list13 = [value for value in range(1,21) if value % 3 ==0]
print(list13)

list13_2 = []
for i in range(1,21):
    if i%3==0:
        list13_2.append(i)
print(list13_2)


#14)下のリストのうち、"c"が含まれている単語だけでリストを作りなさい
list14 = ["abc","dcd", "ef", "gh"]
list14_c = [i for i in list14 if "c" in i] 
#          [#i3 for i2 in list14 if "c" in i1]    
#        append(i) / for i in  /  if "c" in i 
print(list14_c)
        
list14_1_c = []
for i in list14: #i1
    if "c" in i: #i2
        list14_1_c.append(i) #i3
print(list14_1_c)
        
        
#15)下のリストのうち、3、p字以上の単語だけでリストを作りなさい
list15 = ["abc","dcd", "ef", "gh"]
list15_3 = [i for i in list15 if len(i)>=3]
print(list15_3)

list15_1_3 = []
for i in list15:
    if len(i)>=3:
        list15_1_3.append(i)
print(list15_1_3)



#16)1から10までの整数のうち、奇数oddは10を掛けて、偶数evenは２０を掛けたリストを作りなさい
# true if 条件　else false
list16_list = [i*20 if i%2==0 else i*10 for i in range(1,11) ]

list16_1_list = []
for i in range(1,11):
    if i%2==0:
        list16_1_list.append(i*20)
    else:
        list16_1_list.append(i*10)
       
       
