n=int(input())
s=0
for i in range(0,n):
    a=[int(n) for n in input().split()]
    for j in range(0,len(a)):
        s=s+a[j]
#print(s)
m=s/(n*n)
print(m)
print(str.format('{0:.6f}', m))
