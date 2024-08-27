from collections import deque

F,S,G,U,D=map(int,input().split())

def bfs(start_x):
    queue=deque()
    visited=[False]*(F+1)
    queue.append([start_x,0])
    visited[start_x]=True
    while queue:
        x,cnt=queue.popleft()

        if x == G:
            return cnt

        if x+U<=F and not visited[x+U]:
            queue.append([x+U,cnt+1])
            visited[x+U]=True
        if x-D>=1 and not visited[x-D]:
            queue.append([x-D,cnt+1])
            visited[x-D]=True
    
    return 'use the stairs'

print(bfs(S))