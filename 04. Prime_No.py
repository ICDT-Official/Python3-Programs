# PRIME NO. CHECKING USING DEFINITION OR FUNCTION


def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==0):
        return 1
    else:
        return 0

n=int(input("enter a number: "))
if(n==1):
    print("not a prime number")
else:
    p=prime(n)
    if(p==1):
        print("prime number")
    else:
        print("not a prime number")
    
        
        
    
