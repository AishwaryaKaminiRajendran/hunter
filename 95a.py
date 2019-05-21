import math
def isprime(z):
    if(z ==2):
        return True
    elif(z%2 == 0):
        return False
    else:
        for j in range(2,int(math.sqrt(z)+1)):
            if(z%j == 0):
                return False
        return True
n = int(input(""))
prime = []
for i in range(2,n):
    if(isprime(i)):
        prime.append(i)
if(len(prime)>0):
    if(prime[-1] == 97):
        print(" ".join(map(str,prime)),"")
    else:
        print(" ".join(map(str,prime)))
else:
    print(0)
