def fact(n):
    if (n==0 or n==1):
        return 1
    return fact(n-1)*n
    #print(a)
b=int(input("enter a number "))
print(fact(b))
