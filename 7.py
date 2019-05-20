n=int(input())
a=[int(n) for n in input().split()]
for i in range(0,len(a)):
    if a[i]%2==0:
        if i%2!=0:
            print(a[i],end=" ")
    elif a[i]%2!=0:
        if i%2==0:
            print(a[i],end=" ")
