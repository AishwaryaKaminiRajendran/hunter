n=int(input())
a=[int(i) for i in input().split()]
s=a[::-1]
#print(s)
for i in range(0,len(s)):
	print(s[i],end="->")
