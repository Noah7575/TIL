from collections import deque
import math

N = int(input().strip())

if N != 0:
    temp_data = []
    for _ in range(N):
        temp_data.append(int(input().strip()))

    delete = round(N * 15 / 100)

    temp_data.sort()
    data = deque(temp_data)

    # delete 만큼 극단 값 제외
    for _ in range(delete):
        data.pop()
        data.popleft()

    result = round(sum(data) / len(data))

    print(result)

else:
    print(0)