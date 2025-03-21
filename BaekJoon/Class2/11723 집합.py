import sys
input = sys.stdin.readline

M = int(input().strip())

S = set()

for _ in range(M):
    command = list(input().split())

    # add
    if command[0] == 'add':
        S.add(int(command[1]))

    # remove
    elif command[0] == 'remove':
        S.discard(int(command[1]))

    # check
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)

    # toggle
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))

    # all
    elif command[0] == 'all':
        for i in range(1, 21):
            S.add(i)

    # empty
    elif command[0] == 'empty':
        S.clear()
