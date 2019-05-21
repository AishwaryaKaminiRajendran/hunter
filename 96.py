n=int(input())
b=[]
for i in range(1,n):
    for j in range(1,n):
        if i+j==n:
            a=str(i)+str(j)
            b.append(int(a))
print(min(b))
