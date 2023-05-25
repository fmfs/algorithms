# Quicksort Algorithm

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)
