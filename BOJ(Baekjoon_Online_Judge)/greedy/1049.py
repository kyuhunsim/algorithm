import sys
input=sys.stdin.readline

n,m=map(int,input().split())

cnt=0

ls=[]

for i in range(m):
    bundle, one = map(int,input().split())
    ls.append((bundle,one))

min_package_price = min([x[0] for x in ls])
min_single_price = min([x[1] for x in ls])


cost_by_package_only = (n // 6 + 1) * min_package_price

# 2. 패키지와 낱개를 혼합하여 구매하는 경우
cost_by_mixed = (n // 6) * min_package_price + (n % 6) * min_single_price

# 3. 낱개로만 구매하는 경우
cost_by_single_only = n * min_single_price

# 최소 비용 출력
min_cost = min(cost_by_package_only, cost_by_mixed, cost_by_single_only)
print(min_cost)