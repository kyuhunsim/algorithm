N=int(input())
tree = {}  # 딕셔너리로 트리 구조를 저장

for i in range(N - 1):
    u, v = map(int, input().split())
    
    if u not in tree:
        tree[u] = []  # 노드 u가 딕셔너리에 없으면 리스트로 초기화
    if v not in tree:
        tree[v] = []  # 노드 v가 딕셔너리에 없으면 리스트로 초기화
    
    tree[u].append(v)
    tree[v].append(u)

# print(tree)

def dfs(start_node,tree):
    parent=[0]*(N+1)
    stack=[(start_node)]
    visited=set()
    order=[]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in tree[node]:
                if neighbor not in visited:
                    stack.append((neighbor))
                    parent[neighbor]=node

    return visited,order,parent

a=dfs(1,tree)[2]

for i in range(2,N+1):
    print(a[i])