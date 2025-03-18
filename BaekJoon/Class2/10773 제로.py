K = int(input().strip())

stack = []
for i in range(K):
    temp = int(input().strip())
    if temp != 0:
        stack.append(temp)
    else:
        stack.pop()

result = 0
for s in stack:
    result += s

print(result)
