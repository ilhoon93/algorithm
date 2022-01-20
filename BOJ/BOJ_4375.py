while True:
  try:
    n = int(input())
  except EOFError:
    break
  num = 1
  cnt = 1
  while True:
    if num % n == 0:
      print(cnt)
      break
    else:
      num = num * 10 + 1
      cnt += 1