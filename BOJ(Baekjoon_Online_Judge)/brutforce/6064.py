def solve(m, n, x, y):
    while x <= m * n:
        if (x - 1) % n + 1 == y:
            return x
        x += m
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(solve(m, n, x, y))
