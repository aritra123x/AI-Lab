def dfs(ar,n,visited,lst):
    lst.append(n)
    visited[n]=1
    for i in range(len(ar)):
        if visited[i]==0 and ar[n][i]==1:
            dfs(ar,i,visited,lst)
if __name__ == "__main__":
    n=int(input('Enter no of vertices'))
    ar=[]
    print('Enter adjacency matrix')
    for i in range(n):
        row=list(map(int,input().split()))
        ar.append(row)
    s=0
    visited=[0]*n
    lst=[]
    dfs(ar,s,visited,lst)
    print(f"DFS Traversl : {lst}")