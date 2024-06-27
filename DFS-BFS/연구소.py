from collections import deque
import copy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# 바이러스 퍼트리기 (BFS)
def virus(temp, x, y):
  queue = deque([(x, y)])
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if temp[nx][ny] == 0:
          temp[nx][ny] = 2
          queue.append((nx, ny))


# 안전 영역 크기 계산
def get_safe_area(temp):
  return sum(row.count(0) for row in temp)


# 연구실
def lab(count):
  global result
  if count == 3:  # 벽이 3개 설치되면 바이러스 퍼뜨리기
    temp = copy.deepcopy(data)
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(temp, i, j)
    result = max(result, get_safe_area(temp))
    return

  # 벽 세우기
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        lab(count + 1)
        data[i][j] = 0


lab(0)
print(result)
