import heapq

def astar(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, []))
    
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        path = path + [node]

        if node == goal:
            print(f"Optimal Path: {path}")
            print(f"Total Cost: {g}")
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_g = g + weight 
                new_f = new_g + heuristic[neighbor] 
                heapq.heappush(pq, (new_f, new_g, neighbor, path))

    print("No path found!")

if __name__ == "__main__":
    graph = [
        [(1,1), (2,4)],  
        [(2,2), (3,3)], 
        [(4,5)],         
        [(5,2), (6,4)],  
        [(6,3)],        
        [(6,1)],         
        []               
    ]
    
    heuristic = [5, 6, 4, 3, 3, 1, 0]
    start = 0 
    goal = 6   
    
    astar(graph, heuristic, start, goal)
