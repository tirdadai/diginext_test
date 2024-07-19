import ast
m = ast.literal_eval(input())
out = []
for i, j in enumerate(m[:2]):
    n = 0
    for f in m[i+1:]:
        if j[-1] < f[0]:
            out.append((j[0], f[-1]))
        else:
            n += 1
    if n == (len(m) - (i+1)):
        out.append(j)
print(out)
