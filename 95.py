n=int(input())
if n==2:
    print("0")
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
            
