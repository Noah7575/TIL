# 오픈 주소법을 구현하는 해시 클래스 Openhash 사용

from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu: 
    # 메뉴 선택
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep = '    ', end = '')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input("추가할 키: "))
        val = input("추가할 값: ")
        if not hash.add(key, val): # false 이면
            print("추가 실패!")

    elif menu == Menu.삭제:
        key = int(input("삭제할 키: "))
        if not hash.remove(key):
            print("삭제 실패!")
    
    elif menu == Menu.검색:
        key = int(input("검색할 키: "))
        t = hash.search(key)
        if t is not None:
            print(f"검색할 키를 갖는 값은 {t}입니다.")
        else:
            print("검색 실패!")

    elif menu == Menu.덤프:
        hash.dump()

    else:
        break