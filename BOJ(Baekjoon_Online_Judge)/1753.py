import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if distances[current_vertex] < current_distance:
            continue
        
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))
    
    return distances

V, E = map(int, input().strip().split())
K = int(input().strip())
graph = {v: {} for v in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, input().strip().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

distances = dijkstra(graph, K)

for i in range(1, V + 1):
    if distances[i] == float('infinity'):
        print("INF")
    else:
        print(distances[i])
