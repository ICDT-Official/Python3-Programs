n=int(input("enter the value: "))

def fibo():
    a=-1
    b=1
    c=0
    for i in range(0,n):
        c=a+b
        print(c)
        a=b
        b=c
fibo()
        
    
    
