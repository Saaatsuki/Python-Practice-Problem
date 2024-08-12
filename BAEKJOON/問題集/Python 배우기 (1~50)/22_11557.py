T1 = int(input())



for _ in range(T1):
    T2 = int(input())
    school_li = []
    num_li = []
    for _ in range(T2):
        school , num = list(input().split())
        school_li.append(school)
        num_li.append(int(num))
    
    max_idx = num_li.index(max(num_li))
    print(school_li[max_idx])