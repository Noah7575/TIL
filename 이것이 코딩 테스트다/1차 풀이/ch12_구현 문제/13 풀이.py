import itertools

N, M = map(int, input().split())
city = []

# 도시 정보 입력받기
for _ in range(N):
    temp = list(map(int, input().split()))
    city.append(temp)

# 집 좌표와 치킨집 좌표 저장
house_list = []
chicken_list = []

for i in range(N):
    for j in range(M):
        # 집인 경우
        if city[i][j] == 1:
            house_list.append((i, j))
        elif city[i][j] == 2:
            chicken_list.append((i, j))

# 전체 집-치킨 거리 경우의 수 계산해서 저장
whole_dist = [[] for _ in range(len(house_list))]

for i in range(len(house_list)):
    for j in range(len(house_list)):
        dist = abs(house_list[i][0] - chicken_list[i][0]) + abs(house_list[j][0] - chicken_list[j][0])
        whole_dist[i].append(dist)

# 치킨집, 집 번호 매기기
chicken_indexes = []
house_numbs = []
for i in range(len(chicken_list)):
    chicken_indexes.append(i)
for j in range(len(house_list)):
    house_numbs.append(j)

# 치킨집 1개부터 M개까지 조합 경우의 수 리스트
comb_list = [ [] ]
for m in range(1, M+1):
    for comb_index in itertools.combinations(chicken_indexes, m):
        comb_list[m].append(list(comb_index))
    
# 도시거리 최솟값 구하기
city_dist = 0
