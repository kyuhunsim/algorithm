def w(a, b, c, dp):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20, dp)

    if dp[a+50][b+50][c+50] != -1:
        return dp[a+50][b+50][c+50]

    if a < b and b < c:
        dp[a+50][b+50][c+50] = w(a, b, c-1, dp) + w(a, b-1, c-1, dp) - w(a, b-1, c, dp)
    else:
        dp[a+50][b+50][c+50] = w(a-1, b, c, dp) + w(a-1, b-1, c, dp) + w(a-1, b, c-1, dp) - w(a-1, b-1, c-1, dp)

    return dp[a+50][b+50][c+50]

dp = [[[-1]*101 for _ in range(101)] for _ in range(101)]

while True:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        w(a, b, c, dp)
        print(f"w({a}, {b}, {c}) = {w(a,b,c,dp)}")


