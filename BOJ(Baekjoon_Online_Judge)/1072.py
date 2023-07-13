X,Y=map(int,input().split())

if int(100*Y/X)>=99:
    print(-1)

else:
    def binary_search(X,Y):
        start=0
        end=X-1

        while start <= end:
            mid=(start+end)//2
            Z=int(100*Y/X)
            if Z >=int(100*(Y+mid)/(X+mid)):
                start=mid+1
            else:
                end=mid-1
        return end

    print(binary_search(X,Y)+1)
