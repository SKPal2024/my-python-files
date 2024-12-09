num=[1,4,9,16,25,36,49,64,81,100]
print(len(num))
a=int(input("enter a number to check if it exists in the tupple "))
i=0
while i<len(num):
    if(num[i]==a):
       print("the number is at ", i+1)

    i+=1
else:print("number does not exist in the tupple")