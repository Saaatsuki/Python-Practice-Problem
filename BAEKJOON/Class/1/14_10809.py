txt = input()

alp_li = [chr(alp) for alp in range(ord("a"),ord("z")+1)]

for alp in alp_li:
    if alp not in txt:
        print(-1,end=" ")
    else:
        print(txt.index(alp),end=" ")