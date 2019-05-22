n=int(input())
s=0
r=0
k=n
while n>0:
    d=n%10
    s=s+d
    n=n//10
temp=s
#print(temp)
while s>0:
    m=s%10
    r=r*10+m
    s=s//10
temp1=r
#print(temp1)
if temp==temp1:
    print("YES")
else:
    print("NO")
