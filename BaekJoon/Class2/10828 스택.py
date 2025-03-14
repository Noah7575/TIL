from collections import deque

N = int(input().strip())

stack = deque()

for _ in range(N):
    command = list(input().split())
    # push
    if command[0] == 'push':
        stack.append(command[1])
    # pop
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # size
    elif command[0] == 'size':
        print(len(stack))
    # empty
    elif command[0] == 'empty':
        if not stack: # 비어 있으면
            print(1)
        else:
            print(0)
    # top
    elif command[0] == 'top':
        if stack:
            temp = stack.pop()
            print(temp)
            stack.append(temp)
        else:
            print(-1)

    