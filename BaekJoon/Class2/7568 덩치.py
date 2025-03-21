N = int(input().strip())

rank = [1] * N
# 데이터 입력받기 리스트 컴프리헨션
data = [tuple(map(int, input().split())) for _ in range(N)]

# 랭크 채우기
for i in range(N):
    count = 0
    # 덩치가 더 큰 사람이 몇 명인지 센다
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
        else:
            continue
    rank.append(count + 1)

print(" ".join(map(str, rank)))