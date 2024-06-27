from collections import deque

N = int(input())
maps = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
  a, b = map(int, input().split())
  maps[a - 1][b - 1] = 1

turn_time = {}
L = int(input())
for _ in range(L):
  c, d = input().split()
  turn_time[int(c)] = d

move = [0, 1]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def turn_left():
  global move
  left_index = (direction.index(move) - 1) % len(direction)
  move = direction[left_index]


def turn_right():
  global move
  left_index = (direction.index(move) + 1) % len(direction)
  move = direction[left_index]


time = 0
snake = deque([(0, 0)])
x, y = 0, 0
maps[x][y] = 2

while True:
  time += 1

  x += move[0]
  y += move[1]

  # 벽에 부딪히거나 몸에 부딪히면 종료
  if x < 0 or y < 0 or x >= N or y >= N or maps[x][y] == 2:
    break

  # 사과가 없으면 꼬리 제거
  if maps[x][y] == 0:
    i, j = snake.popleft()
    maps[i][j] = 0

  # 이동한 위치에 뱀 머리 추가
  snake.append((x, y))
  maps[x][y] = 2

  # 방향 전환
  if time in turn_time:
    if turn_time[time] == "L":
      turn_left()
    else:
      turn_right()

print(time)
