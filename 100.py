n=int(input())
a=[]
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a.append(i)
#print(a)
c=[]
for k in range(0,len(a)):
    for l in range(0,len(a)):
        if a[k]+a[l]==n:
            b=str(a[k])+' '+str(a[l])
            #print(b)
            c.append(b)
#print(c)
print(c[0])
            
    
    















