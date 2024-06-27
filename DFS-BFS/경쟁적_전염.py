from collections import deque

N, K = map(int, input().split())

graph = []
virus = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

S, X, Y = map(int, input().split())

virus.sort()
q = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus_num, time, x, y = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                q.append((virus_num, time + 1, nx, ny))

print(graph[X-1][Y-1])
