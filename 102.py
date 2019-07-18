
n=int( input( ))
s=0
while n>0:
    d=n%10
    s=s+d*d
    n=n//10
print( s)
