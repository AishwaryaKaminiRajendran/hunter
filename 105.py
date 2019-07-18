
n=int( input( ))
s=0
c=0
t=n
while n>0:
    x=n%10
    c=c+1
    n=n//10
#print( c)   
while t>0:
    d=t%10
    s=s+d**c
    t=t//10
print( s)
