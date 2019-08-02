n=input().split(" ")
a=[]
for i in range(0,len(n)):
    if i%2!=0:
        a.append(n[i])
    else:
        b=n[i][::-1]
        a.append(b)
for j in range(0,len(a)):
    print(a[j],end=" ")

        
