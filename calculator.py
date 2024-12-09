import math
a = int(input("enter 1st number "))
b = int(input("enter 2nd number "))
c = str(input("enter choice "))
#def calculator(a,b):
def calsum(a, b):
    sum = a + b
    print("",a,"+","",b,"=","",sum)
def calsub(a, b):
    sub = a - b
    print("",a,"-","",b,"=","",sub)
def calprod(a, b):
    prod = a * b
    print("",a,"*","",b,"=","",prod)
def caldiv(a, b):
    div = a / b
    print("",a,"/","",b,"=","",div)
def factorial(a):
    #b=int(input(" "))
    i=1
    for d in range(1,a+1):
     i*=d
    print("second number is fALTU just like you")
    print("",a,"!","=",i)
def power(a,b):
    e=pow(a,b)
    print("",a,"^",b,"=",e)
def absolute(a):
    e=abs(a)
    print("second no. is useless just like you")
    print("|",a,"|","=",e)
#    e=a*(-1)
#    if(a<0):
#        print("|",a,"|","=",e)
#    else:print("|",a,"|","=",a)
if(c=="+"):
    print(calsum(a,b))
elif(c=="*"):
    print(calprod(a,b))
elif(c=="-"):
    print(calsub(a,b))
elif(c=="/"):
    if(b==0):
        print("can't devide by 0")
    else:
         print(caldiv(a,b))
elif(c=="!"):
    print(factorial(a))
elif(c=="abs"):
    print(absolute(a))
elif(c=="^"):
    print(power(a, b))
