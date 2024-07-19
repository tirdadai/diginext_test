import ast
Input = ast.literal_eval(input())
Input = sorted(Input)
Output = [] 
temp = [] 
last = -1
for elem in Input:
	if elem - last == 1:
		temp.append(last)
	else:
		temp.append(last)
		Output.append(temp)
		temp = []
	last = elem
ans = []
most = 0
for elem in Output:
	if len(elem)> most:
		most = len(elem)
		ans = elem
print(len(ans))
