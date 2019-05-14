a=int(input())
s=[int(a) for a in input().split()]
j=sorted(s)
i=j[::-1]

for x in range(0,len(i)):
    print(i[x],end="")
