school_count = int(input())
li = []
for _ in range(school_count):
    stu , app = map(int,input().split())
    li.append(app%stu)
print(sum(li))