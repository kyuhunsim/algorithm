from collections import Counter


n=int(input())
ls=[]
for i in range(n):
  a=int(input())
  ls.append(a)
ls.sort()


def find_most(ls):
  c=Counter(ls)
  order=c.most_common()
  max= order[0][1]
  modes=[]
  for num in order:
    if num[1] == max:
      modes.append(num[0])
  modes.sort()

  if len(modes)>1:
    return modes[1]
  else:
    return modes[0]
    
print(round(sum(ls)/n))
print(ls[n//2])
print(find_most(ls))
print(ls[n-1]-ls[0])