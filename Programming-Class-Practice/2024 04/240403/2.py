msg = "Program Start"
print(msg)

def bar(argBar1, argBar2):
    msg1 = "안녕!!!" + foo(argBar1)
    print(msg1)
    
    msg2 = "Hello!!" + foo(argBar2)
    print(msg2)
    
def foo(argFoo):
    msg = argFoo + "님"
    msg = pos(msg)
    return msg

def pos(argPos):
    msg = "*" + argPos + "*"
    return msg

bar("황예지", "Hwang Yeji")
msg = "Program Finish"
print(msg)

