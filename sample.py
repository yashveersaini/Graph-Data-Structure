# Adjacency matrix

n = int(input("Enter no of vertices: "))
m = int(input("Enter no of edges: "))

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

print("Adjacency representation of Graph")
for row in matrix:
    print(row)