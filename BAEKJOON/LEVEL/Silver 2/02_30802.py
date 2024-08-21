import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundles = sum(math.ceil(size / T) for size in sizes)

pen_bundles = N // P
remaining_pens = N % P

print(shirt_bundles)
print(pen_bundles, remaining_pens)
