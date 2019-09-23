'''******
   *    *
   *    *
   *    *
   ******'''

s=""
n=int(input("Enter the value for n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        for j in range(1,n+1):
            s=s+"*"
    else:
        for k in range(1,n+1):
            if(k==1 or k==n):
                s=s+"*"
            else:
                s=s+" "
    s=s+"\n"
print(s)    
    
