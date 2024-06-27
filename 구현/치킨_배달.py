from itertools import combinations
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

result = 1e9

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      house.append([i,j])
    elif graph[i][j] == 2:
      chicken.append([i,j])

for x in combinations(chicken, M):
  compare = 0
  for h in house:
    house_compare = 1e9
    for k in x:
      house_compare = min(house_compare, abs(h[0]-k[0]) + abs(h[1]-k[1]))
    compare += house_compare
  result = min(result, compare)

print(result)
