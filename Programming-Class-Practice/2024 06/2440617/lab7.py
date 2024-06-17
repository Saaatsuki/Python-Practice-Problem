def contains(argList,argNum):
    in_tf = False
    if len([i for i in argList if argNum==i])>0: # argNum in argList
        in_tf = True
    return in_tf
print(contains([1,2,3,4],3))
print(contains([1,2,3,4],8))
