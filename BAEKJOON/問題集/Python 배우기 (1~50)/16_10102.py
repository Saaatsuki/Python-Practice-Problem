num = int(input())
alp_li = list(input())

if alp_li.count("A") == alp_li.count("B"):
    print("Tie")
elif alp_li.count("A") > alp_li.count("B"):
    print("A")
else:
    print("B")