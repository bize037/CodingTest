# 이코테 p.321

n = input()
cnt = len(n) // 2

start = sum(list(map(int, n[:cnt])))
end = sum(list(map(int, n[cnt:])))

if start == end:
  print("LUCKY")
else:
  print("READY")
