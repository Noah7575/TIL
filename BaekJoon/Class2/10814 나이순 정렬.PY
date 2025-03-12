N = int(input().strip())

members = []
for _ in range(N):
    age, name = input().split()
    temp = (int(age), name)
    members.append(temp)

members.sort(key = lambda x: (x[0]))

for member in members:
    print(member[0], member[1])
