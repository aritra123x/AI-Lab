def dls(graph, start,goal, max_depth): 
    traversal=[]
    stack=[(start,0)]
    ans=False
    while stack:
        node,depth=stack.pop()
        if depth<=max_depth:
            traversal.append(node)
            if node==goal:
                ans=True
                break
        else:
            continue
        for i in graph[node]:
            stack.append((i,depth+1))
    return (traversal,ans)


def iddfs(graph, start,goal,n):
    for depth in range(n):
        lst,ans=dls(graph, start,goal,depth)
        print(f"Traversal at depth {depth} : {lst}")
        if ans==True:
            print(f"Goal {goal} is found")
            break
        if len(lst)==n:
            print(f"Goal {goal} is unreachable")
            break


if __name__ == "__main__":
    graph = [[1, 2], [3, 4], [5, 6], [7], [8], [], [9], [], [], []] 
    start = 0
    goal = 9
    n = len(graph)
    iddfs(graph, start,goal,n)
