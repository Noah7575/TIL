# 시퀀스 원소의 최댓값 출력
    # 시퀀스 타입: 리스트, 바이트 배열, 문자열, 튜플, 바이트 열 등

from typing import Any, Sequence
# typing 모듈은 타입 어노테이션을 위해 다양한 타입을 제공
# 그 중에서 Any와 Sequence를 import
# Any: 임의의 자료형

def max_of(a: Sequence) -> Any:
    # a는 시퀀스 타입이고, 반환값은 아무거나 상관없다
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    # 프로그램이 직접 실행되는 경우

    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num
    # 원소수가 num인 리스트 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]값을 입력하세요: "))

    print(f"최댓값: {max_of(x)}")

