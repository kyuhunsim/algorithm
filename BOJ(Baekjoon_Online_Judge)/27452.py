def init_length(length):
    while length[-3] <= 10**18:
        length.append(2 + length[-2] + length[-1])


def solve(n, k):
    if k <= (n + 1) // 2:
        return '('
    elif n < len(length):
        if k == length[n]:
            return ')'
        elif k > length[n]:
            return '0'
        elif k <= length[n-2] + 1:
            return solve(n - 2, k - 1)
        else:
            return solve(n - 1, k - 1 - length[n - 2])
    else:
        temp = (n - len(length) + 3) // 2
        return solve(n - temp*2, k - temp)


length = [0, 2, 2]
init_length(length)
print(length)

for _ in range(int(input())):
    n,k = map(int, input().split())
    print(solve(n,k))