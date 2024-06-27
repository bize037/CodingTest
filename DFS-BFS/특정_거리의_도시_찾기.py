from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

citys = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    citys[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in citys[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

result = [i for i in range(1, n + 1) if distance[i] == k]
if result:
    print('\n'.join(map(str, result)))
else:
    print(-1)
