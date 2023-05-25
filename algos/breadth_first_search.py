# Breadth First Search (BFS) Algorithm

def breadth_first_search(graph, start):
  queue += deque([node])
  visited = set()
  visited.add(start)
  while queue:
    node = queue.popleft()
    print(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)
