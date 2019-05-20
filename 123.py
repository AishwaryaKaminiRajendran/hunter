a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if b[j]==a[i]:
            c=c+1
if c==len(b):
    print("yes")
else:
    print("no")
