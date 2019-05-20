n=int(input())
a=[int(n) for n in input().split()]
b=sorted(a)
for i in range(0,len(b)-1):
    j=i+1
    if b[i]==b[j]:
        print(b[i])
        break
else:
    print("unique")
    
