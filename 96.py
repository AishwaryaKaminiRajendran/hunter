n=int(input())
b=[]
for i in range(0,n+1):
    for j in range(0,n+1):
        if i+j==n:
            a=str(i)+str(j)
            b.append(int(a))
print(min(b))
