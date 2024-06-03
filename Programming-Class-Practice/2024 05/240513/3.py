bar = [2,3,4,5]
foo = (6,7,8,9)

print(bar[0])
print(foo[0])

bar[0] = 20 
foo[60] = 60
print(bar,foo)

for char in (foo:="world"):
    print(char,end="")