from collections import deque

N = int(input().strip())

queue = deque()

for _ in range(N):
    command = list(input().split())
    # push
    if command[0] == 'push':
        queue.append(int(command[1]))
    # pop
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    # size
    elif command[0] == 'size':
        print(len(queue))
    # empty
    elif command[0] == 'empty':
        if not queue: # 비어 있으면
            print(1)
        else:
            print(0)
    # front
    elif command[0] == 'front':
        if queue:
            temp = queue.popleft()
            print(temp)
            queue.appendleft(temp)
        else:
            print(-1)
    # back
    elif command[0] == 'back':
        if queue:
            temp = queue.pop()
            print(temp)
            queue.append(temp)
        else:
            print(-1)

    