def dfs_iterative(adj, V):
    stack = []
    visited = [False]*(V+1)

    stack.append(1)
    visited[1] = True

    while stack:
        top = stack.pop()

        # Adj List is 0-indexed so we take top-1 instead of top
        for n in adj[top-1]:

            # If node is not visited add into stack and mark as visited
            if not visited[n]:
                stack.append(n)
                visited[n] = 1
        
        print(top, end=" ")

    print()

def dfs(adj, v, visited, result):

    visited[v] = True
    result.append(v)

    for n in adj[v-1]:
        if not visited[n]:
            dfs(adj, n, visited, result)
    
    return result
            

adj = [[2,3], [1,4,5], [1], [2,5], [4,2]]
V = 5
dfs_iterative(adj, V)

adj = [[2,3], [1,4,5], [1], [2,5], [4,2]]
V = 5

result = []
visited = [False] * (V+1)
res = dfs(adj, 1, visited, result)
print(res)