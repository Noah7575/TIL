import sys

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]
colors = [i for i in range(3)]
result = int(10e9)

def Backtracking(start, color_record, depth, temp):
    if depth == N:
        return temp
    
    if depth == 1:
        for next_color in colors:
            if next_color != color_record[depth-1]:
                color_record.append(next_color)
                Backtracking(start, color_record, depth + 1, temp + graph[depth][next_color])
                color_record.pop(-1)
    else:
        for next_color in colors:
            if next_color != color_record[depth - 1] and next_color != color_record[depth -2]:
                color_record.append(next_color)
                Backtracking(start, color_record, depth + 1, temp + graph[depth][next_color])
                color_record.pop(-1)
    
    
for color in colors:
    color_record = [color]
    result = min(Backtracking(graph[0][color], color_record, 1, graph[0][color]), result)
    