N,M=map(int,input().split())
ls=list(map(int,input().split()))

def binary_search(array):
    start=max(array)
    end=sum(array)

    while start <= end:
        mid=(start+end)//2
        