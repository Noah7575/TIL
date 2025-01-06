# 퀵 정렬 알고리즘 구현하기 (원소 수가 9 미만이면 단순삽입정렬)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    # a[idx1~3]을 오름차순 정렬하고, 중앙값 인덱스 반환
    if a[idx1] > a[idx2]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx2] > a[idx3]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx1] > a[idx2]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    # 단순 삽입 정렬
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    # a[left] ~ a[right] 퀵 정렬
    if right - left < 9: # 원소수가 9 미만이면
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m] # 피벗

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
           while a[pl] < x: pl += 1
           while a[pr] > x: pr -= 1
           if pl <= pr:
               a[pl], a[pr] = a[pr], a[pl]
               pl += 1
               pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)    


    
