# Binary Search Algorithm

def binary_search(input_list, item):
  low = 0
  high = len(input_list) - 1
  
  while low <= high:
    mid = (low + high) // 2
    guess = input_list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None
