a = [[1, 2], [3, 4], [5, 6]] # 3x2
b = [[1,2,3], [4, 5, 6]] # 2x3

r = []

n = len(a)
m = len(b[0])
p = len(a[0]) # b of row major

for i in range(n):
    rt = []
    for j in range(m):
        result = 0
        for k in range(p):
            result = result + a[i][k] * b[k][j]         
        rt.append(result)
    r.append(rt)

print(r)
