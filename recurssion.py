def show(n):
 if n==0:
  return
 print(n)
 show(n-1)
 print("finished")
a=int(input("enter "))
show(a)