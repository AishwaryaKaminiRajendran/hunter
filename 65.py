n,k=map(int,input().split())
a=[int(n) for n in input().split()]
b=[]
for i in range(0,len(a)):
    if a[i]!=k:
        b.append(a[i])
#print(b)     
if b==[]:
    print("empty")
else:
    for j in range(0,len(b)):
        print(b[j],end=" ")
    
