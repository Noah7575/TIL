
def judge(sentence):
    stack = []
    # 0이면 불균형, 1이면 균형
    for i in sentence:
        if i == '[':
            stack.append(i)
        elif i == '(':
            stack.append(i)

        elif i == ']':
            if stack: # 일단 스택에 뭐가 들어 있어야 함
                temp = stack.pop()
                if temp != '[': #짝이 안 맞으면
                    return 'no'
            else:
                return 'no'

        elif i == ')':
            if stack: # 일단 스택에 뭐가 들어 있어야 함
                temp = stack.pop()
                if temp != '(': #짝이 안 맞으면
                    return 'no'
            else:
                return 'no'

    # 판정이 끝나고 스택에 아무것도 없어야 균형임
    if not stack:
        return 'yes'
    else:
        return 'no'

# 입력 받기
data = []
while True:
    sentence = input()
    if sentence == '.':
        break
    data.append(sentence)

# 판정 출력
for sentence in data:
    print(judge(sentence))

