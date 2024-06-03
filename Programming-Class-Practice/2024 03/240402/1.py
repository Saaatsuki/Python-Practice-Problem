def bar():
    msg = "Hello"
    foo()
    return msg

def foo():
    print("foo")
    pos()
    
def pos():
    print("pos")
    kin()
    
def kin():
    print("kin")
      
bar()