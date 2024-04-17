def say_hello():
    print("皆さん、こんにちは")
say_hello()


def say_hello2(name):
    print(name + "さん、こんにちは")
say_hello2("大野智")


def say_hello3(name):
    print("{}さん、こんにちは".format(name))
say_hello3("櫻井翔")


def calc_square(side):
    return side * side
result_square = calc_square(10)
print(result_square)


import math
def calc_tri(side):
    return (side ** 2) * ((math.sqrt(3)) / 4)
result_tri = calc_tri(10)
print(result_tri)

def calc_tri2(side,high):
    return (side * high * 1/2)
result_tri2 = calc_tri2(10,20)
print(result_tri2)


x = 1
def show_number(a = x):
    print(a)
    
x = 10 # aの値は「1」のまま
show_number()

def shou_number2(a=[]):
    a.append(1)
    print(a,id(a))

shou_number2()
shou_number2()
shou_number2()
shou_number2()



#　位置引数

def shou_number3(a,b,c):
    print(a)
    print(b)
    print(c)
shou_number3(a=1,b=10,c=100)



# 可変長位置引数
# print(),max()でよく使う

def show_number4(a,b,*args):
    print(a)#1
    print(b)#2
    print(args)#(3,4,5)
show_number4(1,2,3,4,5) 

def show_number7(a,b,*args):
    print(a)#1
    print(b)#2
    print(*args)#3,4,5
show_number7(1,2,3,4,5) 

def show_number6(a,b,*args):
    print(a)
    print(b)
    for i in args:
        print(i)
show_number6(1,2,3,4,5) # *args = (3,4,5)複数OK！！
# 出力例
# 1
# 2
# 3
# 4
# 5


#　可変長キーワード引数
def show_number8(**keyword_argments):
    print(keyword_argments)
show_number8(a=1,b=2,c=3)
# {'a': 1, 'b': 2, 'c': 3} #辞書展開

def show_number9(**keyword_argments):
    print(keyword_argments)
dictionary = {"a":1,"b":2,"c":3}
show_number8(**dictionary)
# {'a': 1, 'b': 2, 'c': 3} #辞書展開


#　関数内関数
def outer_func(a,b):
    def inner_func(c,d):
        return c - d
    
    x = inner_func(2,1)
    # y = outer_func(a,b) # この行を削除する
    print(x)

outer_func(3,1)   