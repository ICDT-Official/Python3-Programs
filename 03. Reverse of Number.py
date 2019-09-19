a=int(input("enter a number: "))
rev=0
r=0
while(a>0):
    r=a%10
    rev=rev*10+r
    a=a//10 
print("The reverse of a no is: ",rev) 
    
