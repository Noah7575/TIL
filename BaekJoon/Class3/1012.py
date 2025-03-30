import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(y, x):
    # 인덱스 에러 방지
    if x < 0 or x >= M or y < 0 or y >= N:
        return False 
    # 배추가 있는 경우
    if data[y][x] == 1:
        data[y][x] = 0 # 방문 처리
        # 상하좌우 재귀 호출
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False

T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추밭
    data = [[0]*(M) for _ in range(N)]

    # 배추 좌표 입력 
    for _ in range(K):
        X, Y = map(int, input().split())
        data[Y][X] = 1

    # 필요한 지렁이 세기
    result = 0
    for y in range(N):
        for x in range(M):
           if dfs(y, x) == True:
               result += 1

    print(result)