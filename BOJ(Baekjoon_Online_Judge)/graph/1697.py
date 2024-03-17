from collections import deque

def find_brother(n, k):
    MAX = 100001
    queue = deque([n])
    time = [0] * MAX
    
    while queue:
        x = queue.popleft()
        if x == k:
            return time[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < MAX and not time[nx]:
                time[nx] = time[x] + 1
                queue.append(nx)

# Example input
n, k = map(int,input().split())
print(find_brother(n, k))
