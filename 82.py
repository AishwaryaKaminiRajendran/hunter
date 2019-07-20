n,k=map(int,input().split())
a=[int(n) for n in input().split() ]
b=sorted(a)

for i in range(0,len(b)):
    print(b[i],end=" ")
