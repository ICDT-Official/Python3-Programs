a=[]
b=[]
n=int(input("enter the size of the array: "))
for i in range(0,n):
    m=int(input("enter the numbers of first array: "))
    a.insert(i,m)
print(a[:])
for j in range(0,n):
    c=int(input("enter the numbers of second array: "))
    b.insert(j,c)
print(b[:])
for i in range(0,n):
    flag=0
    for j in range(0,n):
        if(a[i]==b[j]):
            flag=1
            break
    if(flag==1):
        print(a[i])

