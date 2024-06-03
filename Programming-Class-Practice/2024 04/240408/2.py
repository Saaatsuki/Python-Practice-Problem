def bar():
    global local_variable
    local_variable = "지역변수" #地域変数
    print(local_variable)
    
    
global_variable = "전역변수" #Global変数

bar()

print(local_variable)