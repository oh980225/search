# 재귀함수 활용 이진 탐색

def recursive_binary_search(a, x, start, end):
  if start > end:
    return -1 # 남은 탐색 범위가 비었고 결국 찾지 못 했을때

  mid = (start + end) // 2
  if a[mid] == x:
    return mid
  elif a[mid] > x:
    return recursive_binary_search(a, x, start, mid - 1)
  else:
    return recursive_binary_search(a, x, mid + 1, end)