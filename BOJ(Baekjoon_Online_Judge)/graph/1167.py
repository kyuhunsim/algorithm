v=int(input())
ls=[]
tree = {}

# V개의 줄에 걸쳐 간선 정보를 입력받습니다.
for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]  # 첫 번째 값은 정점 번호

    if node not in tree:
        tree[node] = []  # 정점 번호가 아직 딕셔너리에 없으면 빈 리스트로 초기화

    index = 1
    while data[index] != -1:  # -1이 나오기 전까지 간선 정보 읽기
        connected_node = data[index]
        distance = data[index + 1]
        tree[node].append((connected_node, distance))
        index += 2  # 두 개씩 묶어서 읽었으므로 index를 2 증가시킴
print(tree)

def dfs(tree, start_node):
    visited = set()
    stack = [(start_node, 0)]  # (node, current_distance)
    max_distance = 0
    farthest_node = start_node

    while stack:
        node, dist = stack.pop()
        if node not in visited:
            visited.add(node)
            if dist > max_distance:
                max_distance = dist
                farthest_node = node

            for neighbor, distance in tree.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, dist + distance))

    return farthest_node, max_distance

def find_tree_diameter(tree):
    # Step 1: Perform DFS from an arbitrary node (say node 1) to find the farthest node
    start_node = 1
    farthest_node_from_start, _ = dfs(tree, start_node)

    # Step 2: Perform DFS from the farthest node found to get the maximum distance
    farthest_node, tree_diameter = dfs(tree, farthest_node_from_start)

    return tree_diameter

tree_diameter = find_tree_diameter(tree)
print(tree_diameter)