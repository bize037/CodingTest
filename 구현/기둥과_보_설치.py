def is_valid_structure(answer):
  for x, y, structure in answer:
      if structure == 0:
          if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
              continue
          return False
      else:
          if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
              continue
          return False
  return True

def solution(n, build_frame):
  answer = []

  for x, y, structure, operation in build_frame:
      if operation == 1:
          answer.append([x, y, structure])
          if not is_valid_structure(answer):
              answer.remove([x, y, structure])
      else:
          answer.remove([x, y, structure])
          if not is_valid_structure(answer):
              answer.append([x, y, structure])

  answer.sort()
  return answer

