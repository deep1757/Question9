def FInd(l):
    small=l[0]
    for i in range(1,len(l)):
        if small > l[i]:
            small=l[i]
    return small
    
# print(FInd([4,2,5]))    
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    small=FInd(l)
    print(small*(n-1))
