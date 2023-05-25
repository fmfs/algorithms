# Selection Sort Algorithm

def selection_sort(arr):
  new_array = []
  for i in range(len(arr)):
    smallest = find_index_of_smallest(arr)
    new_array.append(arr.pop(smallest))
  return new_array

def find_index_of_smallest(arr):
  smallest = arr[0]
  index_of_smallest = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      index_of_smallest = i
  return index_of_smallest
