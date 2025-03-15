from collections import deque
queue = deque()

N = int(input().strip())

def movie(N):
    result = 665
    count = 0 # 몇 번째 악마의 수인지 판정
    while True:
        result += 1
        # 리스트로 만들어서 판정 시작
        test = str(result)
        if '666' in test:
            count += 1
            if count == N:
                return result
        else:
            continue

        

print(movie(N))


