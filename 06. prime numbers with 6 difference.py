#prime number in range using function with difference 6 between them

a=int(input("enter the starting range: "))
b=int(input("enter the end of the range: "))
p=0
c=[]

for i in range(a,b+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        if(i!=1):
            c.insert(p,i)
            p=p+1

print(c)

for k in range(0,p):
    for m in range(1,p):
        if(c[k]+6==c[m]):
            print(str(c[k])+" "+str(c[m]))




    
    

