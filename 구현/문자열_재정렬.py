# 이코테 p.322

s = input()
chr_list, num_list = [], []

for a in s:
  if ord(a) >= 65:
    chr_list.append(a)
  else:
    num_list.append(a)

chr_list.sort()
num_list.sort()

result = "".join(chr_list + num_list)

print(result)
