MAX_L = 50  
a = [0]*(MAX_L+1)  
p = [0]*(MAX_L+1) 

a[0] = 1
p[0] = 1

for i in range(1, MAX_L+1):
    a[i] = a[i-1]*2 + 3
    p[i] = p[i-1]*2 + 1

def patties_eaten(N, X):
    if X == 0 or N == 0:
        return min(X, 1)
    if X <= a[N-1]+1:
        return patties_eaten(N-1, X-1)
    if X == a[N-1] + 2:
        return p[N-1] + 1
    if X <= 2*a[N-1] + 2:
        return p[N-1] + 1 + patties_eaten(N-1, X - a[N-1] - 2)
    return p[N]



N,X=map(int,input().split())

print(patties_eaten(N, X))  