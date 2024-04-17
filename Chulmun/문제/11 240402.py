msg = "program start"
print(msg)

# 引数argB1とargB2を取るbar関数の定義
def bar(argB1,argB2):#もらうときparameter
    # msg1の定義、"안녕!!!"とfoo(argB1)の結果を結合
    msg1 = "안녕!!!" + foo(argB1)
    print(msg1)
    
    # msg2の定義、"Hello!!!"とfoo(argB2)の結果を結合
    msg2 = "Hello!!!" + foo(argB2)
    print(msg2)

# 引数argFを取るfoo関数の定義
def foo(argF):
     # msgの定義、argFと"님"を結合
    msg = argF + "님"
    # pos関数の結果をmsgに適用
    msg = pos(msg)
    return msg

# 引数argPを取るpos関数の定義
def pos(argP):
    msg = "*" + argP + "*"
    return msg

# bar関数の呼び出し
bar ("황예지","Hwamg Yeji")#あげるときはargument

msg = "program finish"
print(msg)