from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited computers
    queue = deque([start])  # Create a queue and enqueue the starting computer
    infected_count = 0  # Counter for infected computers

    while queue:
        computer = queue.popleft()  # Dequeue a computer from the front of the queue

        if computer not in visited:
            visited.add(computer)  # Mark the computer as visited
            infected_count += 1  # Increment the infected count

            # Enqueue all the directly connected computers that have not been visited
            queue.extend(adjacent for adjacent in graph[computer] if adjacent not in visited)

    return infected_count,visited


# Read the number of computers from input
num_computers = int(input())

# Initialize an empty adjacency list
graph = {i: [] for i in range(1, num_computers + 1)}

# Read the number of pairs of connected computers from input
num_pairs = int(input())

# Read the pairs of connected computers and populate the adjacency list
for _ in range(num_pairs):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

# Call the BFS function with the graph and computer number 1 as the starting point
print(bfs(graph, 1))


print(graph)

