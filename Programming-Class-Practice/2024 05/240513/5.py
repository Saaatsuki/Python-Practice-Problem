# Identity operator
# in, not in
# A in B
# A 값, B sequential Object
# 결과 값은 Boolean

def myInoperator(argValue, argSeqObj):
    for value in argSeqObj:
        if value == argValue:
            return True
    return False


def myInoperator(argValue, argSeqObj):
    pass

print("a" in "abc")

bar = [3, 4, 5, 6]

print(4 in bar)
print(4 not in bar)
print(myInoperator(3, [2, 3, 4]))