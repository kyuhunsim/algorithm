n=int(input())
s=input()
cnt=0
for i in range(n):
    cnt+=(ord(s[i])-ord('a')+1)*(31**i)

print(cnt%1234567891)