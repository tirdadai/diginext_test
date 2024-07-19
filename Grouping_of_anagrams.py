import ast

inp = input()
inp = ast.literal_eval(inp)
out = []
for i in inp:
    m = []

    for j in inp:
        if ''.join(sorted(i)) == ''.join(sorted(j)):
            #print(inp)
            m.append(j)
            #print(j)
            #print(inp)
        else:
            continue
    out.append(m)

def get_unique_values(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(get_unique_values(out))