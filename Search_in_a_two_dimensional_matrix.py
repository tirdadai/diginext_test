import numpy as np
import ast
inp = np.array(ast.literal_eval(input()))
target = int(input())
n = 0
for i in inp:
    for j in i:
        if j == target:
            n += 1
        else:
            continue
if n == 0:
    print("False")
else:
    print("True")
