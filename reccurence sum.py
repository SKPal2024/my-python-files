def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
a=int(input("enter a number "))
print(sum(a))
print((a+1)*a/2)