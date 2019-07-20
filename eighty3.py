n=input()
a=[]
b=[]
for i in range(0,len(n)):
    if n[i]==n[i+1]:
        a.append(n[i])
    else:
        b.append(n[i])
        
