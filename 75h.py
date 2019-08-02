n=int(input())
a=[int(n) for n in input().split()]
for i in range(0,len(a)):
    if i==len(a)-1:
        print(-1,end=" ")
    elif a[i]>a[i+1]:
        print(a[i+1],end=" ")
    else:
        print(-1,end=" ")
