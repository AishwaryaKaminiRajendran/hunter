n=int(input())
a=[int(n) for n in input().split()]
b=sorted(a)
#print(b)
c=b[::-1]
#print(c)
x=[]
for i in range(0,len(c)):
    if c[i]==len(x):
        x.append(c[i])
        break
    else:
        x.append(c[i])
        x.append(b[i])
for j in range(0,len(x)):
    print(x[j],end=" ")
    
