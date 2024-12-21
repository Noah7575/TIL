# 고정 길이 스택 클래스 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum("Menu", ['push', 'pop', 'peak', 'search', 'dump', 'exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end = '')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f"current data : {len(s)} / {s.capacity}")
    menu = select_menu()

    if menu == Menu.push:
        x = int(input("input data: "))
        try:
            s.push(x)
        except FixedStack.Full:
            print("Full!")

    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f"poped data: {x}")
        except FixedStack.Empty:
            print("Empty!")

    elif menu == Menu.peak:
        try:
            x = s.peek()
            print(f"peaked data: {x}")
        except FixedStack.Empty:
            print("Empty!")

    elif menu == Menu.search:
        x = int(input("value to search: "))
        if x in s:
            print(f"count: {s.count(x)}, index: {s.find(x)}")
        else:
            print("can't Find!")

    elif menu == Menu.dump:
        s.dump()

    else:
        break