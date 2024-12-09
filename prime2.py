num=int(input("enter number: "))
a=None
# for i in range(2,x):
#     if x%i==0:
#         a==True
#         break
# if a == True:
#     print("conjugate")
# else:
#     print("prime")
for i in range(2, num):
   if (num % i) == 0:
       a = True
       break
if a==True:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
