
#n=int( input( ))
#s=0
x=0
b=[]
a=int( input( ))
while a>0:
    d=a%10
    b.append( d)
    a=a//10
print( b)
for i in range( 0,len( b)):
    x=x+(b[i]^b[i+1])
print( x)

#for i in range( 0,len( a)):
#while t>0:
#    d=t%10
 #   for i in range( 0,len( a)):
  #      s=s+d**a[i]
   #     break
    #t=t//10
    #i=i+1
#print( s)
