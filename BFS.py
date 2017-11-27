graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = set()
    queue = [start]
    # print('visited: ')
    # print(visited)
    # print('queue: ')
    # print(queue)
    while queue:
        vertex = queue.pop(0)
        # print('vertex:')
        # print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'F')

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    print(queue)
    while queue:
        (vertex, path) = queue.pop(0)
        print(vertex)
        print(path)
        for next in graph[vertex] - set(path):
            print(graph[vertex])
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']