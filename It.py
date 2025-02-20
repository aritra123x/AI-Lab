def dfs_iterative(ar, start):
    n = len(ar)
    visited = [0] * n
    stack = [start]
    dfs=[]
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            dfs.append(node)
            visited[node] = 1
            
            for i in range(n):
                if ar[node][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    break
    print(f"DFS Traversal : {dfs}")
if __name__ == "__main__":
    n = int(input('Enter number of vertices: '))
    ar = []
    print('Enter adjacency matrix:')
    for _ in range(n):
        row = list(map(int, input().split()))
        ar.append(row)
    
    start_vertex = 0
    dfs_iterative(ar, start_vertex)
