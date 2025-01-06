# 병합 정렬 알고리즘 구현

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    # 병합 정렬
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        # a[left] ~ a[right]를 재귀적 병합정렬
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center: 
                # 배열 앞부분을 buff로 복사
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                # 배열 뒷부분과 buff 병합
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1) # 배열 전체 병합 정렬
    del buff # 작업용 배열 소멸

            