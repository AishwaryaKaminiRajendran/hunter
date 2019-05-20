n,m=map(int,input().split())
a=[int(n) for n in input().split()]
b=sorted(a)
c=b[::-1]
print(c[m-1])
