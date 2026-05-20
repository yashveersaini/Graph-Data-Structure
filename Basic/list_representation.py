""" ================== Adjacency list ================ """

n = int(input("Enter no of vertices: "))
m = int(input("Enter no of edges: "))

lst = [[] for _ in range(n+1)]


for _ in range(m):
    u, v = list(map(int, input().split()))
    lst[u].append(v)
    lst[v].append(u)


print("Adjacency list representation of grpah: ")
for i in range(1, n+1):
    print(i, "->", lst[i])

