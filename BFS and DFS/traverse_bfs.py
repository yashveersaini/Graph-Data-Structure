from collections import deque

def bfs(adj, V):

    queue = deque([1])
    visited = [False] * (V+1)
    visited[1] = True

    while queue:
        # First in First out principle
        node = queue.popleft()

        for n in adj[node-1]:

            # If node is not visited then add it into the queue and mark as visited
            if not visited[n]:
                queue.append(n)
                visited[n] = True
        
        print(node, end=" ")
    
    print()


adj = [[2, 6], [1, 3, 4], [2], [2, 5], [4, 7], [1, 7, 8], [5, 6], [6]]
V = 8

bfs(adj, V)
