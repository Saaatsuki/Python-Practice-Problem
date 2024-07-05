con = int(input())

for _ in range(con):
    candy , people = map(int,input().split())
    print(f"You get {candy//people} piece(s) and your dad gets {candy%people} piece(s).")