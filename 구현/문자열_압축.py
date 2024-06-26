# 이코테 P.323
# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
  result = []

  if len(s) == 1:
      return 1

  for i in range(1, len(s) // 2 + 1):
      string = ''
      cnt = 1
      front = s[:i]
      for j in range(i, len(s) + i, i):
          if front == s[j:i+j]:
              cnt += 1
          else:
              if cnt != 1:
                  string = string + str(cnt) + front
              else:
                  string = string + front

              front = s[j:j+i]
              cnt = 1
      result.append(len(string))

  return min(result)
  