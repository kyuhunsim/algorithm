n = int(input())

a, b = map(int, input().split())
m = int(input())

tree = {}

for i in range(m):
    u, v = map(int, input().split())

    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    
    tree[u].append(v)
    tree[v].append(u)

def dfs(start_node, tree):
    distances = [-1] * (n + 1)  # 거리를 저장할 배열 (-1로 초기화)
    stack = [(start_node, 0)]
    visited = set()
    
    while stack:
        node, dist = stack.pop()
        if node not in visited:
            visited.add(node)
            distances[node] = dist  # 해당 노드까지의 거리 저장
            for neighbor in tree[node]:
                if neighbor not in visited:
                    stack.append((neighbor, dist + 1))

    return distances

# DFS 실행 (a번 노드에서 시작하여 거리를 계산)
distances_from_a = dfs(a, tree)

# b번 노드까지의 거리 출력
distance_to_b = distances_from_a[b]

if distance_to_b != -1:
    print(distance_to_b)
else:
    print(-1)
