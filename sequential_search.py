def search_list(a, x):
  n = len(a)
  for i in range(0, n):
    if x == a[i]:
      return i
  return -1