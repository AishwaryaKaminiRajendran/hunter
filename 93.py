n=input()
a=list(n)
#print(a)
j=0
b=[]
for i in range(0,len(a)):
    if a[i]!=" ":
        j=j+1
    if j%2==1:
        b.append(a[i].upper())
    else:
        b.append(a[i])
#print(b)
for k in range(0,len(b)):
    print(b[k],end="")
