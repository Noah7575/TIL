N = int(input().strip())

words = []

for _ in range(N):
    words.append(input().strip())

# 중복 제거
set_words = set(words)
words = list(set_words)

# 정렬
words.sort(key = lambda x: (len(x), x))

for word in words:
    print(word)
