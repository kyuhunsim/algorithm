from collections import deque

n = int(input())
deq = deque()
tmp = []
for i in range(n):
    a = input().split()
    if a[0] == '1':
        deq.append(int(a[1]))
        tmp.append([len(deq), deq[-1]])
    elif a[0] == '2':
        if len(deq) != 0:
            deq.popleft()
        if len(deq) > 0:  # Check here before accessing the last element
            tmp.append([len(deq), deq[-1]])



tmp=sorted(tmp,key=lambda x: x[0],reverse=True)
print(*tmp[0])
