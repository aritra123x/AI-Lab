def bfs(ar, source):
    n = len(ar)
    visited = [0] * n
    queue = [source]
    lst = [] 

    while queue:
        node = queue.pop(0) 
        if visited[node] == 0:
            visited[node] = 1
            lst.append(node) 
            
            for i in range(n):  
                if ar[node][i] == 1 and visited[i] == 0:
                    queue.append(i) 

    print(f"BFS Traversal: {lst}")

# Driver Code
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    ar = []
    print("Enter the adjacency matrix:")
    for _ in range(n):
        lst = list(map(int, input().split()))
        ar.append(lst)
    
    source = 0 
    bfs(ar, source)
