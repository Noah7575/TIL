N = int(input().strip())

datasets = []
for _ in range(N):
    x, y = map(int, input().split())
    datasets.append((x, y))

datasets.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
    print(datasets[i][0], datasets[i][1])