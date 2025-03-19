M, N = map(int, input().split())

sieve = [False] * 2 + [True] * (N-1)
prime_list = []

for i in range(N+1):
    if sieve[i] : #True면
        # 배수 없애고
        for j in range(i * 2, N+1, i):
            sieve[j] = False
        # M보다 크면 리스트에 넣어준다
        if i >= M:
            prime_list.append(i)

for p in prime_list:
    print(p)