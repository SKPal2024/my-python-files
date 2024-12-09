from array import *
arr=array('i',[])
n=int(input("enter length-> "))
for i in range(n):
    a=int(input("enter number: "))
    arr.append(a)
print(arr)
for i in range(n):
    print(i , arr[i])