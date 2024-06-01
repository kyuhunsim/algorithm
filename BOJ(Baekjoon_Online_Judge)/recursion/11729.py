def hanoi(n, source, tmp, target):
    if n > 0:
        
        hanoi(n - 1, source, target, tmp)
        
        
        print('%s %s' % (source, target))
        
        
        hanoi(n - 1, tmp, source, target)

N=int(input())
print(2**N-1)
hanoi(N, '1', '2', '3')
