ki,qu,lu,bi,ni,po = map(int,input().split())

out_ki = 1-ki
out_qu = 1-qu
out_lu = 2-lu
out_bi = 2-bi
out_ni = 2-ni
out_po = 8-po

print(f"{out_ki} {out_qu} {out_lu} {out_bi} {out_ni} {out_po}")

# chess = [1, 1, 2, 2, 2, 8]
# lst = list(map(int, input().split()))

# for i in range(len(chess)) :
#     chess[i] -= lst[i]
# print(*chess)
