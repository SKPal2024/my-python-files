a=int(input("enter last even numbers "))
b=1
while b<a:
     if(b%2!=0):
         b = b + 1
         continue
     print(b)
     b+=1
