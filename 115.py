n=int(input())
a=[]
c=0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a.append(i)
for k in range(0,len(a)):
    for l in range(k,len(a)):
        if a[k]+a[l]==n:
            c=c+1
print(c)
