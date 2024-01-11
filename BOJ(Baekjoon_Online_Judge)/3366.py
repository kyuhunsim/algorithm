n = int(input())
arr = [int(input()) for _ in range(n)]
stack = [int(1e9) + 1]
ans = 0

i = 0
while i < n:
    if arr[i] < stack[-1]:
        stack.append(arr[i])
    else:
        if stack[-2] > arr[i]:
            ans += arr[i]
            stack[-1] = arr[i]
        else:
            ans += stack[-2]
            stack.pop()
            continue
    i += 1

for i in range(len(stack) - 1, 1, -1):
    ans += stack[i - 1]

print(ans)