star = int(input())

for i in range(1,star+1):
    print(f"{'*'*i}{' '*(star-i)}{' '*(star-i)}{'*'*i}")
for i in range(1,star):
    print(f"{'*'*(star-i)}{' '*i}{' '*i}{'*'*(star-i)}")    