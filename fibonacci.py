a=0
b=1
nxt=None
n=int(input("enter number "))
for i in range(1,n+1,1):
    print(a)
    nxt=a+b
    a=b
    b=nxt
