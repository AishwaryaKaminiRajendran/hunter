n=int(input())
a=[int(n) for n in input().split()]
b=min(a)
c=max(a)
for i in range(0,len(a)):
    if a[i]==b:
        print(i+1,end=" ")
for j in range(0,len(a)):
    if a[j]==c:
        print(j+1,end=" ")
    
