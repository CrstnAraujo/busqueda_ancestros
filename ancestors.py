import sys

# === Lectura de datos === #
option = None
while option not in (1, 2):
    option = int(input("Read from:\t\nterminal (1)\t\ndocument (2)\t\nexit (3): "))
    if option ==  3: sys.exit(0)
    
if option == 1:
    input_data = sys.stdin.read().split()
else:
    input_data = ['4', '5', '1', '3', '3', '2', '2', '4', '1', '4', '4', '4', '4', '1', '3', '4', '4', '3']
    
n = int(input_data[0])
q = int(input_data[1])

if len(input_data) != 2*n + 2*q:
    sys.exit("Ammount of entries were incorrect.")


# === Representación árbol mediante lista de adyacencia === #
edges = [[] for _ in range(n + 1)]
for i in range(2, 2*n - 1, 2):
    u = int(input_data[i])
    v = int(input_data[i + 1])
    print(f'u: {u}, v: {v}')
    edges[u].append(v) 
    edges[v].append(u)


# === Recorrido en profundidad y registro tiempos entrada/salida === #
time = 1
time_out = [0] * (n + 1)
time_in = [0] * (n + 1)
stack = [(1, False, -1)]

while stack:
    node, visited, parent = stack.pop()
    if not visited:
        time_in[node] = time
        time += 1
        visited = True
        stack.append((node, visited, parent))
        for neighbour in edges[node]:
            if neighbour != parent:
                stack.append((neighbour, False, node))
    else:
        time_out[node] = time
        time += 1

output = []
for i in range(2*n, len(input_data), 2):
    u = int(input_data[i])
    v = int(input_data[i + 1])
    if time_in[u] <= time_in[v] and time_out[u] >= time_in[v]:
        output.append("YES")
    else:
        output.append("NO")

print(output)