N = int(input().strip())

data = []
for i in range(N):
    data.append(input().strip())

def VPS(datum):
    stack = []
    for d in datum:
        if d == '(':
            stack.append(d)
        elif d == ')':
            # 앞에 (가 있으면
            if stack:
                stack.pop()
            else:
                return 'NO'
    # 판정이 끝나면 스택은 비어 있어야 함
    if not stack:
        return 'YES'
    else:
        return 'NO'


for datum in data:
    print(VPS(datum))