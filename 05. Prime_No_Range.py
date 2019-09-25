# PRIME NO. CHECKING IN A RANGE USING DEFINITION OR FUNCTION

a=int(input("enter the starting range: "))
b=int(input("enter the end of the range: "))

def prime(n):
    for i in range(a,n+1):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
    if(flag==0):
        return 1
    else:
        return 0

for i in range(a,b+1):
    p=prime(i)
    if(p==1 and i!=1):
        print(i)
    
    
        
        
    
