""" ================== Adjacency matrix ================ """

n = int(input("Enter no of vertices: "))
m = int(input("Enter no of edges: "))

matrix = [[0]*(n+1) for _ in range(n+1)]

# Undirected Graph
for i in range(m):
    u, v = list(map(int, input().split()))
    matrix[u][v] = 1
    matrix[v][u] = 1


# Directed Graph
# for i in range(m):
#     u, v = list(map(int, input().split()))
#     matrix[u][v] = 1


print("Adjacency representation of Graph")
for row in matrix[1:]:
    print(row[1:])

