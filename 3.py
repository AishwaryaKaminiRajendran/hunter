n=int(input())
a=[int(n) for n in input().split()]
c=0
b=[]
for i in range(0,len(a)):
    if a[i]==i:
        c=c+1
        b.append(a[i])
if c==0:
    print("-1")
else:
    for j in b:
        print(j,end=" ")
        
