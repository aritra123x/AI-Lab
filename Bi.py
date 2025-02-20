from collections import deque

# Function for BFS traversal
def bfs(queue, visited, parent, graph):
    current = queue.popleft()
    for vertex in graph[current]:
        if not visited[vertex]:
            queue.append(vertex)
            visited[vertex] = True
            parent[vertex] = current

# Check for intersection between forward and backward searches
def is_intersecting(src_visited, dest_visited, vertices):
    for i in range(vertices):
        if src_visited[i] and dest_visited[i]:
            return i
    return -1

# Print the path from source to destination
def print_path(intersecting_node, src, dest, src_parent, dest_parent):
    path = []
    i = intersecting_node
    while i != src:
        path.append(i)
        i = src_parent[i]
    path.append(src)
    path.reverse()
    
    i = intersecting_node
    while i != dest:
        i = dest_parent[i]
        path.append(i)
    
    print(f"Path : {path}")

# Function to perform bidirectional search
def bidirectional_search(graph, src, dest, vertices):
    src_queue = deque([src])
    dest_queue = deque([dest])
    
    src_visited = [False] * vertices
    dest_visited = [False] * vertices
    
    src_parent = [-1] * vertices
    dest_parent = [-1] * vertices
    
    src_visited[src] = True
    dest_visited[dest] = True
    
    while src_queue and dest_queue:
        bfs(src_queue, src_visited, src_parent, graph)
        bfs(dest_queue, dest_visited, dest_parent, graph)
        
        intersecting_node = is_intersecting(src_visited, dest_visited, vertices)
        if intersecting_node != -1:
            print(f"Path exists between {src} and {dest}")
            print(f"Intersection at: {intersecting_node}")
            print_path(intersecting_node, src, dest, src_parent, dest_parent)
            return
    
    print(f"Path does not exist between {src} and {dest}")

# Driver code
if __name__ == '__main__':
    graph = [[4], [4], [5], [5], [0, 1, 6], [2, 3, 6], [4, 5, 7], [6, 8], 
             [7, 9, 10], [8, 11, 12], [8, 13, 14], [9], [9], [10], [10]]
    
    src, dest = 0, 14
    bidirectional_search(graph, src, dest, len(graph))
