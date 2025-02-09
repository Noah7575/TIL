n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 부족하면 더 많이 자르기
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이니까 여기서 기록
        start = mid + 1

print(result)
